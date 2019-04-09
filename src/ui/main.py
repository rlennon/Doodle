from flask import Flask, render_template, url_for, flash, redirect, request
from ui import Forms
import json
import requests


app = Flask(__name__)

app.config['SECRET_KEY'] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'

uname = 'admin'
pword = 'admin'
url = 'http://10.216.202.10:5000'


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = Forms.LoginForm()
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
    requirements = {}
    form = Forms.AddForm()
    if 'addEditClearRequirement' in request.form:
        if form.validate_on_submit():
            if form.requirement.data == "" and form.description.data == "":
                requirements = {}
                form.branchRequirements.data = ""
            elif form.description.data == "" and form.requirement.data != "" and form.branchRequirements.data != "":
                requirements = json.loads(form.branchRequirements.data)
                del requirements[form.requirement.data]
                form.requirement.data = ""
                form.description.data = ""
                form.branchRequirements.data = json.dumps(requirements)
            elif form.description.data != "" and form.requirement.data == "" and form.branchRequirements.data != "":
                print('here')
                requirements = json.loads(form.branchRequirements.data)
            else:
                print('last')
                if form.branchRequirements.data != "":
                    requirements = json.loads(form.branchRequirements.data)
                requirements[form.requirement.data] = form.description.data
                form.requirement.data = ""
                form.description.data = ""
                form.branchRequirements.data = json.dumps(requirements)
            return render_template("create.html", form=form, requirements=requirements)
    if 'submit' in request.form:
        if form.validate_on_submit():
            flash('Branch Created', 'success')
            urlpost = url+"/requirement"
            if form.branchRequirements.data != "":
                requirements = json.loads(form.branchRequirements.data)
            requirements['name'] = form.name.data
            requirements['location'] = form.location.data
            requirements['contact'] = form.contact.data
            requests.post(urlpost, json=requirements)
            return redirect(url_for('home'))

    return render_template("create.html", form=form, requirements=requirements)


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
                'location': doc['location']
            }
        )
    return render_template("home.html", branches=branches)


@app.route("/branch/<branchid>", methods=['GET', 'POST'])
def update(branchid):
    form = Forms.UpdateForm()
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
