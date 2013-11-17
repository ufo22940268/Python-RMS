#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 ccheng <ccheng@cchengs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""

"""

import json
import requests
import random
from pymongo import *

BASE_URL = "http://127.0.0.1:5000/"
#BASE_URL = "http://192.241.196.189/"
AUTH = ("asdf", "asdf")

def get_url(s):
    return BASE_URL + s

class End(object):

    def __init__(self, end):
        if not end:
            raise Exception('End is necessary.')
        self.end = end
        self.url = BASE_URL + end

    def clear(self):
        requests.delete(self.url, auth=AUTH)

    def generate_snum(self):
        return self.end.upper() + str(random.randrange(100000))

    def add(self, d, snum = False):
        if snum and not d.get('snum'):
            d['snum'] = self.generate_snum()
        p = {'item1': str(json.dumps(d))}
        r = requests.post(self.url, p, auth=AUTH)
        if  json.loads(r.text)['item1']['status'] != "OK":
            raise Exception(r.text)

    def get(self, params={}):
        r = requests.get(self.url, auth=AUTH, params=params)
        return json.loads(r.text)['_items']

    def get_one(self):
        a = self.get()
        if a and len(a):
            return a[0]

def get_db():
    client = MongoClient('localhost')
    db = client['rms']
    return db
