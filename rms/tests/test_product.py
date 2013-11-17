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

product = End('product')
imports = End('import')
exports = End('export')
warning_product = End('warning_product')
TEST_PRODUCT_SNUM = "prodcut_123"

def setup_module():
    imports.clear();
    exports.clear();
    product.clear()


def test_main():
    product.add({'name': 'p', 'snum': TEST_PRODUCT_SNUM})

    add(TEST_PRODUCT_SNUM)
    assert get_count(TEST_PRODUCT_SNUM) == '1'

    minus(TEST_PRODUCT_SNUM)
    assert get_count(TEST_PRODUCT_SNUM) == '0'

def add(snum):
    imports.add({'product_name': 'ipn', 'product_snum': snum}, snum = True)

def minus(snum):
    exports.add({'product_name': 'epn', 'product_snum': snum}, snum = True)

def get_count(snum):
    return product.get()[0]['num']

@pytest.fixture
def init():
    imports.clear();
    exports.clear();
    product.clear()

#def test_get_above_minimun(init):
    #product.add({'name': 'p', 'snum': TEST_PRODUCT_SNUM, 'num': '5', 'max': '4'})
    #product.add({'name': 'p', 'snum': 'product22222', 'num': '35', 'max': '4'})

def test_warning_product(init):
    product.add({'name': 'p1', 'snum': TEST_PRODUCT_SNUM, 'num': '5', 'min': '6'})
    product.add({'name': 'p2', 'snum': 'product22222', 'num': '35', 'min': '4'})
    product.add({'name': 'p3', 'snum': 'product22223', 'num': '5', 'min': '6'})

    len(warning_product.get()) == 1
    warning_product.get()[0]['name'] = 'p1'

    items = warning_product.get({'max_results': 1, 'page': 1})
    assert items[0]['name'] == 'p1'
    assert len(items) == 1

def test_warning_product2(init):
    product.add({'name': 'p1', 'snum': TEST_PRODUCT_SNUM, 'num': '5', 'max': '6'})
    product.add({'name': 'p2', 'snum': 'product22222', 'num': '35', 'max': '4'})
    product.add({'name': 'p3', 'snum': 'product22223', 'num': '5', 'max': '6'})

    len(warning_product.get()) == 1
    warning_product.get()[0]['name'] = 'p2'

    items = warning_product.get({'max_results': 1, 'page': 1})
    assert items[0]['name'] == 'p2'
    assert len(items) == 1
