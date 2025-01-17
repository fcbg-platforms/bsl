[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![codecov](https://codecov.io/gh/fcbg-platforms/bsl/graph/badge.svg?token=grHKQLaeei)](https://codecov.io/gh/fcbg-platforms/bsl)
[![tests](https://github.com/fcbg-platforms/bsl/actions/workflows/pytest.yml/badge.svg?branch=maint/0.6)](https://github.com/fcbg-platforms/bsl/actions/workflows/pytest.yml)
[![doc](https://github.com/fcbg-platforms/bsl/actions/workflows/doc.yml/badge.svg?branch=maint/0.6)](https://github.com/fcbg-platforms/bsl/actions/workflows/doc.yml)
[![PyPI version](https://badge.fury.io/py/bsl.svg)](https://badge.fury.io/py/bsl)
[![Downloads](https://static.pepy.tech/personalized-badge/bsl?period=total&units=international_system&left_color=grey&right_color=blue&left_text=pypi%20downloads)](https://pepy.tech/project/bsl)
[![Downloads](https://static.pepy.tech/personalized-badge/bsl?period=month&units=international_system&left_color=grey&right_color=blue&left_text=pypi%20downloads/month)](https://pepy.tech/project/bsl)

> [!WARNING]
> This project is discontinued in favor of [MNE-LSL](https://github.com/mne-tools/mne-lsl).

[![Brain Streaming Layer](https://raw.githubusercontent.com/fcbg-platforms/bsl/maint/0.6/doc/_static/icon-with-name/icon-with-name.svg)](https://fcbg-platforms.github.io/bsl)

**BrainStreamingLayer** [(Documentation website)](https://fcbg-platforms.github.io/bsl)
provides a real-time brain signal streaming framework.
**BSL** contains an improved python-binding for the Lab Streaming Layer C++ library,
`bsl.lsl`, replacing `pylsl`. This low-level binding is used in high-level objects to
interact with LSL streams.

Any signal acquisition system supported by native LSL or OpenVibe is also
supported by BSL. Since the data communication is based on TCP, signals can be
transmitted wirelessly. For more information about LSL, please visit the
[LSL github](https://github.com/sccn/labstreaminglayer).

# Install

BSL supports `python ≥ 3.8` and is available on [PyPI](https://pypi.org/project/bsl/).
Install instruction can be found on the
[documentation website](https://fcbg-platforms.github.io/bsl/dev/install.html).

# Acknowledgment

**BSL** is based on **NeuroDecode**. The original version developed by
[**Kyuhwa Lee**](https://github.com/dbdq) was recognised at
[Microsoft Brain Signal Decoding competition](https://github.com/dbdq/microsoft_decoding)
with the First Prize Award (2016) after achieving high decoding accuracy.
**BSL** is based on the refactor version by
[**Arnaud Desvachez**](https://github.com/dnastars) for the
[Fondation Campus Biotech Geneva (FCBG)](https://github.com/fcbg-platforms) and
development is still supported by the
[M/EEG-Neuromodulation platform (FCBG)](https://fcbg.ch/).

<img src="https://raw.githubusercontent.com/fcbg-platforms/bsl/maint/0.6/doc/_static/partners/FCBG.svg" width=150>

# Copyright and license

The code is released under the [MIT License](https://opensource.org/licenses/MIT).
