#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 ccheng <ccheng@cchengs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""

"""

import account
from db import *
from flask import request

def before_import(document):
    product_snum = document[0]['product_snum']
    if get_db().product.find({'snum': product_snum}).count() == 0:
        create_product_from_import(document)
    else:
        get_db().product.update(
                {'snum': product_snum},
                {'$inc': {'num': document[0]['quantity']}}
                )

def create_product_from_import(doc):
    m = {
            'product_snum': 'snum',
            'product_name': 'name',
            'color': 'color',
            'property': 'property',
            'comment': 'comment',
            'provider': 'company',
            'quantity': 'num',
        }


    if not doc:
        return

    raw = doc[0]
    new = dict()
    for k, v in raw.items():
        if k in m:
            new[m[k]] = v

    insert_with_auth_field(get_db().product, new)
