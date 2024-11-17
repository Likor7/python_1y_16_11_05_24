from flask import Flask, render_template

app = Flask(__name__)

subject = "Python"

group_name = "1y_16_11_05_24"

students = [
    {"name": "Sophia", "gender": "female", "age": 15},
    {"name": "Semen", "gender": "male", "age": 13},
    {"name": "Andrii", "gender": "male", "age": 17},
    {"name": "Vlad", "gender": "male", "age": 16},
    {"name": "Vova", "gender": "male", "age": 15},
    {"name": "Rostyslav", "gender": "male", "age": 14},
]


@app.route("/")
def index():
    context = {
        "title": "GoIteens",
        "subject": subject,
        "group_name": group_name,
        "students": students,
    }
    return render_template("./index.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
