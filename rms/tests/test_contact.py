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

contact_end = End('contact')

def setup_module():
    contact_end.clear()

def test_add():
    for i in range(10):
        contact_end.add({'name': str(i), 'tel': str(12)})
