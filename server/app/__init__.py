from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 7870

    from app.routes import main
    app.register_blueprint(main)

    return app
 