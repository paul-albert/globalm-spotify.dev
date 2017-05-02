# Main script

from flask import Flask

from config import config_instance
from controllers import controllers


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_instance)
    config_instance.init_app(app)
    app.secret_key = config_instance.APP_SECRET_KEY
    app.register_blueprint(controllers,
                           url_prefix='',
                           config=config_instance)
    return app


if __name__ == '__main__':
    app_instance = create_app()
    app_instance.run(host=config_instance.APP_HOST,
                     port=config_instance.APP_PORT,
                     debug=config_instance.DEBUG,
                     use_reloader=config_instance.USE_RELOADER)
