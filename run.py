from rms import rms

host = "127.0.0.1"
port = 5000
Bootstrap(rms.app)
rms.app.register_blueprint(eve_docs, url_prefix='/docs')
rms.app.run(host=host, port=port, debug=True)
