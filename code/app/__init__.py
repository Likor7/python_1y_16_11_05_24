from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

login_manager = LoginManager()
db = SQLAlchemy()


def create_app():
    from .views import main_blueprint, auth_blueprint, blog_blueprint
    from .models import User, AnonymousUser

    app = Flask(__name__)

    # app.config.from_object()
    app.config["APP_NAME"] = "Flask Blog"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_bloh.db"
    app.config["SECRET_KEY"] = "Dsamdkasmdk127al32mkdm32ska$82"
    app.config["WTF_CSRF_ENABLED"] = False

    # Setup extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(blog_blueprint)

    @login_manager.user_loader
    def get_user(id):
        return User.query.get(int(id))

    login_manager.login_view = "auth.signin"
    login_manager.login_message_category = "info"
    login_manager.anonymous_user = AnonymousUser

    @app.errorhandler(HTTPException)
    def handle_http_error(exc):
        return render_template("error.html", error=exc), exc.code

    return app
