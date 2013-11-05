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

def test_super_user_id():
    sid = op_end.get()[0].get('super_user_id')
    assert sid
    
def test_operator():
    op = op_end.get()[0]
    assert op['name'] == 'k' and op['password'] == 'k'

def test_login():
    r = requests.post(get_url("login"), {'name': 'k', 'password': 'k'})
    assert r.text

#def test_get_list():
    #r = requests.get(get_url("import"), auth=('k', 'k'))
    #json.loads(r.text)
