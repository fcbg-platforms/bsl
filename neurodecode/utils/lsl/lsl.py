from __future__ import print_function, division

"""
LSL wrapper functions for creating a server and a client.
"""
import pylsl
import multiprocessing as mp
from neurodecode import logger

#----------------------------------------------------------------------
def start_server(server_name, n_channels=1, channel_format='string', nominal_srate=pylsl.IRREGULAR_RATE, stype='Markers',
                 source_id=None):
    """
    Start a new LSL server.

    Parameters
    ----------
    server_name : str
        Name of the server
    n_channels : int
        Number of channels
    channel_format : str
        The channels' format ('string', 'float32', 'double64', 'int8', 'int16', 'int32', 'int64')
    nominal_srate : float
        Sampling rate in Hz
    stype : str
        Signal type
    source_id : str
        If None, set to server name

    Returns
    -------
    LSL outlet :
        LSL server object
    """
    if source_id is None:
        source_id = server_name
        
    sinfo = pylsl.StreamInfo(server_name, channel_count=n_channels, channel_format=channel_format,\
                           nominal_srate=nominal_srate, type=stype, source_id=source_id)
    return pylsl.StreamOutlet(sinfo)

#----------------------------------------------------------------------
def start_client(server_name, state=mp.Value('i', 1)):
    """
    Search for an LSL outlet (server) and open an LSL inlet (client).

    Parameters
    ----------
    server_name: str
        Name of the server to search
    state : Multiprocessing.Value 
        Used to stop searching from another process.

    Returns
    -------
    LSL inlet:
        LSL client object
    """
    while state.value == 1:
        logger.info('Searching for LSL server %s ...' % server_name)
        streamInfos = pylsl.resolve_byprop("name", server_name, timeout=1)
        
        if not streamInfos:
            continue
        
        for sinfo in streamInfos:
            logger.info('Found %s' % sinfo.name())
        sinfo = streamInfos[0]
        break
    
    return pylsl.StreamInlet(sinfo)

#----------------------------------------------------------------------
def list_lsl_streams(ignore_markers=False, logger=logger, state=mp.Value('i', 1)):
    """
    List all the available outlets on LSL network.
    
    Parameters
    ----------
    ignore_markers : bool
        If True, ignore streams with Marker type
    logger : logging.Logger
        The logger to output info
    state: mp.Value
        The multiprocess sharing variable, used to stop search from another process
    """
    import time

    # look for LSL servers
    amp_list = []
    amp_list_backup = []

    while state.value == 1:
        
        streamInfos = pylsl.resolve_streams()
        
        if len(streamInfos) > 0:
            
            for index, si in enumerate(streamInfos):
                amp_name = si.name()
                if 'Markers' in si.type():
                    amp_list_backup.append((index, amp_name))
                else:
                    amp_list.append((index, amp_name))
            break
        
        logger.info('No server available yet on the network...')
        time.sleep(1)

    if ignore_markers is False:
        amp_list += amp_list_backup

    logger.info('-- List of servers --')
    
    for i, (index, amp_name) in enumerate(amp_list):
        logger.info('%d: %s' % (i, amp_name))

    return amp_list, streamInfos

#----------------------------------------------------------------------
def search_lsl(ignore_markers=False, logger=logger, state=mp.Value('i', 1)):
    """
    Search and select an available stream on LSL network
    
    Does not open a LSL inlet.
    
    Parameters
    ----------
    ignore_markers : bool
        If True, ignore streams with Marker type
    logger : logging.Logger
        The logger to output info
    state: mp.Value
        The multiprocess sharing variable, used to stop search from another process
    
    Returns:
    --------
    str : The selected amp name
    """
    amp_list, streamInfos = list_lsl_streams(ignore_markers, logger, state)

    if len(amp_list) == 1:
        index = 0
    else:
        index = input('Amp index? Hit enter without index to select the first server.\n>> ')
        if index.strip() == '':
            index = 0
        else:
            index = int(index.strip())
    
    amp_index, amp_name = amp_list[index]
    si = streamInfos[amp_index]
    assert amp_name == si.name()
    
    logger.info('Selected: %s' % (amp_name))

    return amp_name

#----------------------------------------------------------------------
def lsl_channel_list(inlet):
    """
    Extract the channels name list from the LSL info.

    Parameters
    ----------
    inlet : pylsl.StreamInlet
        The inlet to extract channels list
        
    Returns:
    --------
    list : List of channels name [ name1, name2, ... ]
    """
    if not type(inlet) is pylsl.StreamInlet:
        logger.error('Wrong input type %s' % type(inlet))
        raise TypeError

    ch = inlet.info().desc().child('channels').first_child()
    ch_list = []
    for k in range(inlet.info().channel_count()):
        ch_name = ch.child_value('label')
        ch_list.append(ch_name)
        ch = ch.next_sibling()
    
    return ch_list