#coding:utf-8
from base import *
import os
import requests
from pymongo import *
import pytest
from bson.objectid import ObjectId
import json

excel_url_end = End('excel_url')
def test_print_import():
    excel_file = 'rms/static/files/a.xls'
    if os.path.isfile(excel_file):
        os.remove(excel_file)

    r = excel_url_end.get_raw(params={'table': 'import'})
    assert r.status_code == 200
    result = json.loads(r.text)['result']
    assert result
    assert result['excel']

    assert os.path.isfile(excel_file)
