# -*- coding: utf-8 -*-

from eve import Eve

import os
import json
import account
from flask import request
from eve.auth import BasicAuth
from eve.auth import TokenAuth

app = None

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
            method):
        operators = app.data.driver.db['operator']
        super_users = app.data.driver.db['super_user']
        user = operators.find_one({'name': username})
        if user:
            self.request_auth_value = user['super_user_id']
        else: 
            user = super_users.find_one({'name': username})
            if user:
                self.request_auth_value = user['_id']

        return user and user['password'] == password

app = Eve(settings='rms/settings.py', auth=MyBasicAuth)
#app = Eve(settings='rms/settings.py')

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
        permissions = one.get('permission')
    else:
        msg = 'login failed'
        token =  ""
        status = 404
        permissions = []

    result = {"msg": msg, "token": token, "status": status, 'permissions': permissions}
    if sid:
        result['super_user_id'] = sid
    return json.dumps(result)

#app.on_POST_operator = account.update_super_user_id
