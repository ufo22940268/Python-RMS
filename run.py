# -*- coding: utf-8 -*-
import os
from eve import Eve
from eve.auth import BasicAuth
from eve.auth import TokenAuth
from flask.ext.bootstrap import Bootstrap
from eve_docs import eve_docs


class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
            method):
        return username == 'admin' and password == 'secret'

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000

    #app = Eve(auth=MyBasicAuth)
    app = Eve()
    Bootstrap(app)
    app.register_blueprint(eve_docs, url_prefix='/docs')
    app.run(host=host, port=port, debug=True)
