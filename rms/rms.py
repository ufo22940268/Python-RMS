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


app = None

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
            method):
        operators = app.data.driver.db['operator']
        super_users = app.data.driver.db['super_user']
        user = operators.find_one({'name': username})

        if user and user.get('super_user_id'):
            self.request_auth_value = user['super_user_id']
        else:
            user = super_users.find_one({'name': username})
            if user:
                self.request_auth_value = user['_id']

        return user and user['password'] == password

app = Eve(settings='rms/settings.py', auth=MyBasicAuth)
app.on_insert_import = product.before_import

@app.before_request
def log_request():
    log = "HEADERS:\t\n" + str(request.headers) + "\n"
    if request.form:
        log += "\nFORMS:\t\n" + str(request.form);
    current_app.logger.debug(log)


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
    else:
        msg = 'login failed'
        token =  ""
        status = 404
        info = dict()

    result = {"msg": msg, "token": token, "status": status, 'info': info}
    if sid:
        result['super_user_id'] = sid
    return json.dumps(result)

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
