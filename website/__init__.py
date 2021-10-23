from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'npsdderfamnws'

    from .website_routes import views

    app.register_blueprint(views, url_pref='/')

    return app
