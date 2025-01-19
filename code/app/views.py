from flask import render_template, Blueprint, request
from .controllers import AnswerController
from .forms import SurveyForm

main_blueprint = Blueprint("main", __name__)

# data = {
#     "question": "What web framework do u use?",
#     "fields": ["Flask", "FastAPI", "Django", "ASP.NET"],
# }


@main_blueprint.route("/")
def index():
    form = SurveyForm()
    return render_template("index.html", form=form)


@main_blueprint.route("/poll", methods=["GET", "POST"])
def poll():
    form = SurveyForm()
    if form.validate_on_submit():
        AnswerController.create_answer(
            request.remote_addr, form.question.label.text, form.question.data
        )
    return render_template(
        "greetings.html", vote=form.question.data, question=form.question.label.text
    )
