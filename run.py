# -*- coding: utf-8 -*-

"""
    Eve Demo
    ~~~~~~~~

    A demostration of a simple API powered by Eve REST API.

    The live demo is available at eve-demo.herokuapp.com. Please keep in mind
    that the it is running on Heroku's free tier using a free MongoHQ
    sandbox, which means that the first request to the service will probably
    be slow. The database gets a reset every now and then.

    :copyright: (c) 2012 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

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


class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        """For the purpose of this example the implementation is as simple as
        possible. A 'real' token should probably contain a hash of the
        username/password combo, which sould then validated against the account
        data stored on the DB.
        """
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        return accounts.find_one({'token': token})

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000

    app = Eve(auth=MyBasicAuth)
    app = Eve()
    Bootstrap(app)
    app.register_blueprint(eve_docs, url_prefix='/docs')
    app.run(host=host, port=port, debug=True)
