from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField


class SurveyForm(FlaskForm):
    question = RadioField(
        "What web framework do u use?",
        choices=[
            ("Flask", "Flask"),
            ("FastAPI", "FastAPI"),
            ("Django", "Django"),
            ("ASP.NET", "ASP.NET"),
        ],
    )

    submit = SubmitField("Vote")
