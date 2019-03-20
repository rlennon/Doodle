from flask import Flask, render_template, url_for, flash, redirect
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'

uname = 'admin'
pword = 'admin'

branches = [
        {
            'id': 1,
            'name': 'Doodle Branch',
            'location': 'Letterkenny'
        },
        {
            'id': 2,
            'name': 'Doodle DataCenter',
            'location': 'Buncrana'
        },
        {
            'id': 3,
            'name': 'Doodle Car Park',
            'location': 'Letterkenny'
        }
    ]


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class AddForm(FlaskForm):
    name = StringField('Branch Name', validators=[DataRequired(), Length(min=2, max=20)])
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Create')


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == uname and form.password.data == pword:
            flash('Successfully Logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect Details', 'danger')
            return redirect(url_for('login'))

    return render_template("login.html", form=form)


@app.route("/create/", methods=['GET', 'POST'])
def create():
    form = AddForm()
    if form.validate_on_submit():
        flash('Branch Created', 'success')
        branch = {'id': 4, 'name': form.name.data, 'location': form.location.data}
        branches.append(branch)
        return redirect(url_for('home'))

    return render_template("create.html", form=form)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", branches=branches)


if __name__ == "__main__":
    app.run(debug=True)
