#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 ccheng <ccheng@cchengs-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

"""

Common utils for eve.

"""
from datetime import datetime

def new_snum(end):
    time = datetime.today().strftime("%Y%m%d%H%M%S")
    return end + "_" + "NS" + time
