from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db_bloh.db"

db.init_app(app)

title = "Блог"


@app.route("/")
def index():
    return render_template("./index.html", title=title)


if __name__ == "__main__":

    # Відповідний код для створення табличок
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    app.run(debug=True)
