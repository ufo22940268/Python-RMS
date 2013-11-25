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
import pytest
import requests

order_end = End('order')
open_order_end = End('open_order')
product = End('product')
exports_end = End('export')

@pytest.fixture
def init_order():
    product.clear()
    product.add({'name': 'p', 'snum': '1'})
    order_end.clear()
    open_order_end.clear()
    exports_end.clear()

def test_open_order_validated(init_order):
    order_end.add({'product_name': 'name', 'product_snum': '1', 'validated': '1'}, snum = True)
    assert open_order_end.get_one()
    assert open_order_end.get_one()['product_name'] == 'name'

def test_open_order_unvalidated(init_order):
    order_end.add({'product_name': 'name', 'product_snum': '1', 'validated': '0'}, snum = True)
    assert open_order_end.get_one() == None

@pytest.mark.current
def test_add_order(init_order):
    r = order_end.add({'product_name': 'name', 'product_snum': '1', 'validated': '0'}, snum = True)
    item_id = r['item1']['_id']
    assert not exports_end.get_one()

@pytest.mark.current
def test_add_delivered_order(init_order):
    init_product_p()
    r = order_end.add({'product_name': 'name', 'product_snum': 'p',
        'validated': '0', 'status': 'seller_delivered'}, snum = True)
    item_id = r['item1']['_id']
    ex = exports_end.get_one()
    assert ex
    assert ex['snum'].find('export_') == 0

    #Can't make eve recognize the list i inserted into databse manually.
    #order = order_end.get_one()
    #assert len(order['exports_snum'])
