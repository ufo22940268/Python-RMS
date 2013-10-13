# -*- coding: utf-8 -*-

from eve import Eve

import os
import json
import account
from flask import request
from eve.auth import BasicAuth
from eve.auth import TokenAuth

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
            method):
        return account.exists(username, password)

app = Eve(settings='rms/settings.py', auth=MyBasicAuth)
#app = Eve(settings='rms/settings.py')

@app.route('/login', methods=['POST'])
def login():
    name = request.form['name']
    password = request.form['password']
    one = account.get_one(name, password)
    if one:
        msg = 'login succeed'
        token =  "Basic ", account.create_credential(name, password)
        status = 200
        permissions = one.get('permission')
    else:
        msg = 'login failed'
        token =  ""
        status = 404
        permissions = ['read', 'add', 'delete', 'validate']

    return json.dumps({"msg": msg, "token": token, "status": status, 'permissions': permissions})

#app.on_POST_account = account.add_credential_for_post

#if __name__ == '__main__':
    #if deploy.is_local():
        ## let's not forget the API entry point
        #host = "127.0.0.1"
    #else:
        #host = "192.241.196.189"

    #port = 5000

    ##app = Eve(auth=MyBasicAuth)

    #app.run(host=host, port=port, debug=True)

