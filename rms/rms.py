# -*- coding: utf-8 -*-

from eve import Eve

import os
import json
import account
import product
from flask import request
from eve.auth import BasicAuth
from eve.auth import TokenAuth
import validate
from flask import request, current_app
import deploy
from bson.json_util import dumps
import itertools


app = None

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
            method):
        operators = app.data.driver.db['operator']
        super_users = app.data.driver.db['super_user']
        user = operators.find_one({'name': username})

        #Auth value is to indicate which field is used to store the identification of resource. This affects the all kinds of request following.
        if user:
            self.request_auth_value = user['super_user_id']
        else:
            user = super_users.find_one({'name': username})
            if user:
                self.request_auth_value = user['_id']

        return user and user['password'] == password

if deploy.is_local():
    app = Eve(settings='rms/settings.py', auth=MyBasicAuth)
else:
    app = Eve(settings='/root/rms/settings.py', auth=MyBasicAuth)

app.on_insert_import = product.before_import
app.on_insert_export = product.before_export
app.on_POST_operator = account.update_super_user_id

#@app.before_request
#def log_request():
    #log = "HEADERS:\t\n" + str(request.headers) + "\n"
    #if request.form:
        #log += "\nFORMS:\t\n" + str(request.form);
    #current_app.logger.debug(log)


@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    password = request.form['password']
    one = account.get_one(name, password)
    sid = account.get_super_user_id(name, password)
    if one:
        msg = 'login succeed'
        token =  "Basic " + account.create_credential(name, password)
        status = 200
        info = dict()
        for k, v in one.items():
            if k.find("permission") != -1:
                info[k] = v
        info['_id'] = str(one['_id'])
    else:
        msg = 'login failed'
        token =  ""
        status = 404
        info = dict()
            
    result = {"msg": msg, "token": token, "status": status, 'info': info}
    if sid:
        result['super_user_id'] = sid
    return json.dumps(result)

@app.route('/warning_product', methods=['GET'])
def warning_product():
    product = app.data.driver.db['product']
    plist = []
    for p in list(product.find()):
        if p.get('min'):
            if to_int(p['num']) < to_int(p['min']):
                plist.append(p)
                break

        if p.get('max'):
            if to_int(p['num']) > to_int(p['max']):
                plist.append(p)
                break

    max_results = int(request.args.get('max_results', 0))
    page = int(request.args.get('page', 1))
    if max_results:
        plist = list(getrows_byslice(plist, max_results))[page - 1]
    r = dumps({'_items': plist})

    return r

def getrows_byslice(seq, rowlen):
    for start in xrange(0, len(seq), rowlen):
        yield seq[start:start+rowlen]

def to_int(s):
    return int(s) if s else 0

@app.route('/validate_import', methods=['POST'])
def validate_import():
    ids = json.loads(request.form['ids'])
    validate.validate('import', ids)
    return "success"

@app.route('/validate_export', methods=['POST'])
def validate_export():
    ids = json.loads(request.form['ids'])
    validate.validate('export', ids)
    return "success"

@app.route('/validate_order', methods=['POST'])
def validate_order():
    ids = json.loads(request.form['ids'])
    validate.validate('order', ids)
    return "success"

@app.route('/validate_open_order', methods=['POST'])
def validate_open_order():
    ids = json.loads(request.form['ids'])
    validate.validate('open_order', ids)
    return "success"

@app.route('/get_password', methods=['GET'])
def get_password():
    if not request.args.get('name') and not request.args.get('mobile'):
        return json.dumps({'status': '204', '_items': '[]'})

    operators = app.data.driver.db['operator']
    super_users = app.data.driver.db['super_user']
    op = operators.find_one({'name': request.args.get('name'), 'mobile': request.args.get('mobile')})
    su = super_users.find_one({'name': request.args.get('name'), 'mobile': request.args.get('mobile')})
    if op:
        al = op
    else:
        al = su
    if al:
        pwd = al['password']
        return json.dumps({'status': '204', '_items': {'password': pwd}})
    else:
        return json.dumps({'status': '204', '_items': '[]'})
