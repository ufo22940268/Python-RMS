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
from bson.objectid import ObjectId
import json

def before_import(document):
    product_snum = document[0]['product_snum']
    if get_db().product.find({'snum': product_snum}).count() == 0:
        create_product_from_import(document)
    else:
        one = get_db().product.find({'snum': product_snum})
        if one.count() != 0:
            one = one[0]
            o_num = int(one['num']) if one.get('num') else 0
            n_new = int(document[0]['quantity'])
            num = str(o_num +  n_new)
            get_db().product.update(
                    {'snum': product_snum},
                    {'$set': {'num': num}}
                    )

def before_export(document):
    product_snum = document[0]['product_snum']
    if get_db().product.find({'snum': product_snum}).count() == 0:
        create_product_from_import(document)
    else:
        one = get_db().product.find({'snum': product_snum})
        if one.count() != 0:
            one = one[0]
            o_num = int(one['num']) if one.get('num') else 0
            n_new = int(document[0]['quantity'])
            num = str(o_num -  n_new)
            get_db().product.update(
                    {'snum': product_snum},
                    {'$set': {'num': num}}
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
    new['num'] = int(raw['quantity'])

    insert_with_auth_field(get_db().product, new)

def insert_or_update_order(request, payload):
    data = json.loads(payload.data)
    order_id = data['item1']['_id']

    order = get_db().order.find_one({'_id': ObjectId(order_id)})
    if not order: 
        return

    if order['status'] == 'seller_delivered' or order['status'] == 'repo_delivered':
        add_order_to_imports(order)

def is_product_exists(snum):
    return get_db().product.find_one({'snum': snum})

def add_order_to_imports(order):
    if not order.get('product_snum'):
        return

    if not is_product_exists(order['product_snum']):
        return

    get_import().insert({
        'snum': order['product_snum'],
        'quantity': order.get('quantity'),
        'product_name': order.get('product_name'),
        'provider': order.get('contact'),
        })
