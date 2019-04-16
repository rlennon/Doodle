from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class AddForm(FlaskForm):
    name = StringField('Branch Name', validators=[DataRequired(), Length(min=2, max=20)])
    location = TextAreaField('Location', validators=[DataRequired(), Length(min=2, max=200)])
    contact = StringField('Contact', validators=[DataRequired(), Length(min=1, max=20)])
    requirement = StringField('Requirement')
    description = TextAreaField('Description/Value')
    branchRequirements = TextAreaField('branchRequirements')
    submit = SubmitField('Create')
    addEditClearRequirement = SubmitField('Add / Edit / Clear Requirement')


class UpdateForm(FlaskForm):
    name = StringField('Branch Name')
    location = StringField('Location')
    width = StringField('Width')
    length = StringField('Length')
    height = StringField('Height')

    submit = SubmitField('Update')
    delete = SubmitField('Delete')
