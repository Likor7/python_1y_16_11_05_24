import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


db = SQLAlchemy()


def create_app(env="development"):
    from .views import main_blueprint

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "sqlite:///" + os.path.join(BASE_DIR, "development.sqlite3"),
    )

    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY", "Wow, it should have a secret key"
    )

    db.init_app(app)

    # Register Blueprint
    app.register_blueprint(main_blueprint)

    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template("error.html", error=exc), exc.code

    return app
