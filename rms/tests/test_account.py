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
from pymongo import *
import pytest
from bson.objectid import ObjectId

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

def init_super_user():
    db = get_db()
    db.super_user.drop()
    return db.super_user.insert({'name': 'asdf', 'password': 'asdf'})

def test_login():
    sid = init_super_user()
    db = get_db()
    db.operator.drop()
    db.super_user.insert({'name': 'k', 'password': 'k', 'super_user_id': ObjectId(sid)})

    #Operator
    r = requests.post(get_url("login"), {'name': 'k', 'password': 'k'})
    assert r.text
    js = json.loads(r.text)
    assert js['info']['_id']

    #Super user
    r = requests.post(get_url("login"), {'name': 'asdf', 'password': 'asdf'})
    js = json.loads(r.text)
    assert js['info']['_id']

    db.operator.drop()

#def test_get_operator_password():
    #db = get_db()
    #db.operator.drop()
    #db.operator.insert({'name': 'asdf', 'password': 'asdf', 'super_user_id': '123123'})
    #r = requests.get(get_url('get_password'), params={'name': 'asdf'})
    #js = json.loads(r.text)
    #assert js['status'] == 200
    #assert js['password']

def test_get_password():
    init_super_user()
    r = requests.get(get_url('get_password'), params={'name': 'asdf'})
    js = json.loads(r.text)
    js['status'] == 200

    r = requests.get(get_url('get_password'), params={'name': 'asdf', 'mobile': 'asdfasdf'})
    js = json.loads(r.text)
    js['status'] != 200

    r = requests.get(get_url('get_password'))
    js = json.loads(r.text)
    js['status'] != 200

    db = get_db()
    assert db.super_user.find().count() > 0

