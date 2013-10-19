#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 ccheng <ccheng@cchengs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""

"""
import os

def is_local():
    return os.environ['USER'].find('ccheng') != -1 or os.environ['USER'].find('garlic') != -1
