#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 ccheng <ccheng@cchengs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""

"""

from base import *
import requests

record_end = End('record')

def setup_module():
    record_end.clear()

def test_add():
    for i in range(10):
        record_end.add({'DialNum': str(i), 'CallerID':'asdfijiji'})
