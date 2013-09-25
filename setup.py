#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 ccheng <ccheng@cchengs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""

"""
from setuptools import setup

setup(
    name='rms',
    version='1.0',
    long_description=__doc__,
    packages=['rms', 'eve_docs'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
