from flask import Flask, render_template, url_for, flash, redirect, request
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'

uname = 'admin'
pword = 'admin'
url = 'http://api.internal.tld:8080'


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class AddForm(FlaskForm):
    name = StringField('Branch Name', validators=[DataRequired(), Length(min=2, max=20)])
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=20)])
    width = StringField('Width', validators=[DataRequired(), Length(min=1, max=20)])
    length = StringField('Length', validators=[DataRequired(), Length(min=1, max=20)])
    height = StringField('Height', validators=[DataRequired(), Length(min=1, max=20)])

    submit = SubmitField('Create')


class UpdateForm(FlaskForm):
    name = StringField('Branch Name')
    location = StringField('Location')
    width = StringField('Width')
    length = StringField('Length')
    height = StringField('Height')

    submit = SubmitField('Update')
    delete = SubmitField('Delete')


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
        urlpost = url+"/requirement"
        branch = {
            'name': form.name.data,
            'location': form.location.data,
            'width': form.width.data,
            'length': form.length.data,
            'height': form.height.data
        }
        requests.post(urlpost, json=branch)
        return redirect(url_for('home'))

    return render_template("create.html", form=form)


@app.route("/")
@app.route("/home")
def home():
    urlget = url+"/requirements"
    response = requests.get(urlget)
    col = response.json()
    branches = []

    for doc in col:
        branches.append(
            {
                'id': doc['_id']["$oid"],
                'name': doc['name'],
                'location': doc['location'],
                'width': doc['width'],
                'length': doc['length'],
                'height': doc['height']
            }
        )
    return render_template("home.html", branches=branches)


@app.route("/branch/<branchid>", methods=['GET', 'POST'])
def update(branchid):
    form = UpdateForm()
    if 'submit' in request.form:
        if form.validate_on_submit():
            urlput = url+"/requirement"
            updatedbranch = {
                'name': form.name.data,
                '_id': {
                    '$oid': branchid
                },
                'location': form.location.data,
                'width': form.width.data,
                'length': form.length.data,
                'height': form.height.data,
                'lan connections': '16'
            }
            r = requests.put(urlput, json=updatedbranch)
            print(r.status_code)
            print(r.content)
            flash('Successfully Updated', 'success')
            return redirect(url_for('home'))
        else:
            print('helloworld')
    elif 'delete' in request.form:
        deleteAction(branchid)
        flash('Successfully Deleted', 'success')
        return redirect(url_for('home'))

    urlget = url+"/requirement?_Id=%s" % branchid
    response = requests.get(urlget)
    col = response.json()

    details = {
        'id': col['_id']["$oid"],
        'name': col['name'],
        'location': col['location'],
        'width': col['width'],
        'length': col['length'],
        'height': col['height']
    }
    return render_template("update.html", details=details, form=form)


def deleteAction(branchid):
    urldelete = url+"/requirement?_Id={}".format(branchid)
    requests.delete(urldelete)


if __name__ == "__main__":
    app.run(debug=True)
