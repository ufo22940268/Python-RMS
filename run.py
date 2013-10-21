from rms import rms
from rms import deploy
from eve_docs import eve_docs
from flask.ext.bootstrap import Bootstrap

host = deploy.get_host()
port = 5000
Bootstrap(rms.app)
rms.app.register_blueprint(eve_docs, url_prefix='/docs')
rms.app.run(host=host, port=port, debug=True)
