from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    task = StringField('Task',validators=[DataRequired()])
    assignee = StringField('Assignee',validators=[DataRequired()])
    assigner = StringField('Assigner',validators=[DataRequired()])
    description = TextAreaField('Description',validators=[DataRequired()])
    submit = SubmitField()