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
