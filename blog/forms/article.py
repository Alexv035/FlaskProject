from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField, validators


class CreateArticleForm(FlaskForm):
    tags = SelectMultipleField("Tags", coerce=int)
