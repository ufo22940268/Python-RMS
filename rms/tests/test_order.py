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

def setup_module():
    product.clear()
    product.add({'name': 'p', 'snum': '1'})
    order_end.clear()
    open_order_end.clear()

@pytest.mark.order
def test_add():
    order_end.add({'product_name': 'name', 'product_snum': '1'}, snum = True)
    assert open_order_end.get_one()
    assert open_order_end.get_one()['product_name'] == 'name'

