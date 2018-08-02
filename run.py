import os
from app import create_app
from app import connect
from werkzeug.contrib.fixers import ProxyFix


config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name=config_name)
app.wsgi_app = ProxyFix(app.wsgi_app)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    connect()
    app.run(host="0.0.0.0", port=port)

