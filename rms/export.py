#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 ccheng <ccheng@cchengs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import xlwt
import arrow
import os
import os.path

def export_to_excel(data):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    for row, x in enumerate(data):
        for col, k in enumerate(x.keys()):
            if type(x[k]) != dict:
                ws.write(row, col, x[k])

    static_dir = 'rms/static/files'
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    #Write to this file for test.
    wb.save('%s/a.xls' % static_dir)
    filename = str(arrow.utcnow().timestamp) + ".xls"
    wb.save('%s/%s' % (static_dir, filename))
    return filename
