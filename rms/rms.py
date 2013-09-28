# -*- coding: utf-8 -*-

from eve import Eve
app = Eve(settings='rms/settings.py')

import os
import json
import account
from eve.auth import BasicAuth
from eve.auth import TokenAuth

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
            method):
        return username == 'admin' and password == 'secret'

app.on_POST_account = account.add_credential_for_post

#if __name__ == '__main__':
    #if deploy.is_local():
        ## let's not forget the API entry point
        #host = "127.0.0.1"
    #else:
        #host = "192.241.196.189"

    #port = 5000

    ##app = Eve(auth=MyBasicAuth)

    #app.run(host=host, port=port, debug=True)

