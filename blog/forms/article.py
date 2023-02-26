
from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField, validators
from flask_wtf import FlaskForm

class CreateArticleForm(FlaskForm):
    title = StringField(
        "Title",
        [validators.DataRequired()],
    )
    body = TextAreaField(
        "Body",
        [validators.DataRequired()],
    )
    submit = SubmitField("Publish")
    tags = SelectMultipleField("Tags", coerce=int)

