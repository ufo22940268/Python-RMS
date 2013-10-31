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

BASE_URL = "http://127.0.0.1:5000/"
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

    def add(self, d):
        p = {'item1': str(json.dumps(d))}
        requests.post(self.url, p, auth=AUTH)

    def get(self):
        r = requests.get(self.url, auth=AUTH)
        return json.loads(r.text)['_items']
