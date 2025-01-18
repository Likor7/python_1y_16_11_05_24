from flask import Flask, render_template, request

app = Flask(__name__)

data = {
    "question": "What web framework do u use?",
    "fields": ["Flask", "FastAPI", "Django", "ASP.NET"],
}

filename = "survey.txt"


@app.route("/")
def index():
    return render_template("index.html", data=data)


@app.route("/poll")
def poll():
    vote = request.args.get("field")
    with open(filename, "a") as file_out:
        file_out.write(f"{vote}\n")
    return render_template("greetings.html", vote=vote, question=data["question"])


if __name__ == "__main__":
    app.run(debug=True)
