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

op_end = End('operator')

def setup_module():
    op_end.clear()
    op_end.add({'name': 'k', 'password':'k'})

def test_operator():
    op = op_end.get()[0]
    assert op['name'] == 'k' and op['password'] == 'k'

def test_login():
    r = requests.post(get_url("login"), {'name': 'k', 'password': 'k'})
    print r.text
    assert r.text
