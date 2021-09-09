from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import Length


class PostCreateForm(FlaskForm):
    title = StringField('title', validators=[Length(max=20, min=4, message="Must be between 4 and 20")])
    description = TextAreaField('description', validators=None)
