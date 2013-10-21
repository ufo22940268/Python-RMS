from rms import rms
from eve_docs import eve_docs
from flask.ext.bootstrap import Bootstrap

host = "192.168.1.102"
port = 5000
Bootstrap(rms.app)
rms.app.register_blueprint(eve_docs, url_prefix='/docs')
rms.app.run(host=host, port=port, debug=True)
