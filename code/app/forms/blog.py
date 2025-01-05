from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField("Title", [DataRequired(), Length(4, 256)])
    content = TextAreaField("Content", [DataRequired()])
    submit = SubmitField("Publish")
