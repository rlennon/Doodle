import os
import Forms
import json
import requests
import base64
import datetime
from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)
isAuthenticated = False
app.config['SECRET_KEY'] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'

if 'DOODLE_CONFIG' in os.environ:
    filepath = os.environ['DOODLE_CONFIG']
else:
    filepath = '../config.json'

with open(filepath) as f:
    config = json.load(f)

hostIp = config.get("apiHost")
port = config.get("apiPort")
url = "http://{}:{}".format(hostIp, port)
loginArray = config.get("login")
logins = {}
for login in loginArray:
    logins[login["uname"]] = base64.b64decode(login["pword"])


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = Forms.LoginForm()
    if form.validate_on_submit():
        print(logins[form.username.data] == form.password.data)
        if form.username.data in logins and logins[form.username.data].decode("utf-8") == form.password.data:
            global isAuthenticated
            isAuthenticated = True
            session_data = {}
            session_data["login_date"] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            session_data["uname"] = form.username.data
            urlpost = url + "/session"
            session_id = requests.post(urlpost, json=session_data)
            print(session_id)
            flash('Successfully Logged in', 'success')
            return redirect(url_for('home/{}'.format(session_id)))
        else:
            flash('Incorrect Details', 'danger')
            return redirect(url_for('login'))

    return render_template("login.html", form=form, authenticated=isAuthenticated)


@app.route("/")
@app.route("/home/<session_id>")
def home(session_id):
    if isAuthenticated is False:
        flash('Please Login', 'danger')
        return redirect(url_for('login'))
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
                'contact': doc['contact']
            }
        )
    return render_template("home.html", branches=branches, authenticated=isAuthenticated)

@app.route("/create/", methods=['GET', 'POST'])
def create():
    if isAuthenticated is False:
        flash('Please Login', 'danger')
        return redirect(url_for('login'))
    requirements = {}
    form = Forms.AddForm()
    if 'addEditClearRequirement' in request.form:
        if form.validate_on_submit():
            if form.branchRequirements.data != "":
                requirements = json.loads(form.branchRequirements.data)
            else:
                requirements = {}

            if form.requirement.data == "" and form.description.data == "":
                requirements = {}
                form.branchRequirements.data = ""

            elif form.description.data == "" and form.requirement.data != "" and form.branchRequirements.data != "" \
                    and form.requirement.data in requirements:
                del requirements[form.requirement.data]
                form.requirement.data = ""
                form.description.data = ""
                form.branchRequirements.data = json.dumps(requirements)

            elif form.description.data != "" and form.requirement.data == "":
                pass
            else:
                requirements[form.requirement.data] = form.description.data
                form.requirement.data = ""
                form.description.data = ""
                form.branchRequirements.data = json.dumps(requirements)
            return render_template("create.html", form=form, requirements=requirements, authenticated=isAuthenticated)
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

    return render_template("create.html", form=form, requirements=requirements, authenticated=isAuthenticated)


@app.route("/branch/<branchid>", methods=['GET', 'POST'])
def update(branchid):
    if isAuthenticated is False:
        return redirect(url_for('login'))
    form = Forms.UpdateForm()

    urlget = url + "/requirement?_Id=%s" % branchid
    response = requests.get(urlget)
    branch = response.json()
    id = branch['_id']
    if 'addEditClearRequirement' in request.form:
        if form.validate_on_submit():
            if form.branchRequirements.data != "":
                requirements = json.loads(form.branchRequirements.data)
            else:
                requirements = {}

            if form.requirement.data == "" and form.description.data == "":
                requirements = {}
                form.branchRequirements.data = ""

            elif form.description.data == "" and form.requirement.data != "" and form.branchRequirements.data != "" \
                    and form.requirement.data in requirements:
                del requirements[form.requirement.data]
                form.requirement.data = ""
                form.description.data = ""
                form.branchRequirements.data = json.dumps(requirements)

            elif form.description.data != "" and form.requirement.data == "":
                pass
            else:
                requirements[form.requirement.data] = form.description.data
                form.requirement.data = ""
                form.description.data = ""
                form.branchRequirements.data = json.dumps(requirements)
            return render_template("update.html", form=form, requirements=requirements, edit="true", authenticated=isAuthenticated)
    elif 'update' in request.form:
        if form.validate_on_submit():
            flash('Branch Updated', 'success')
            urlput = url+"/requirement"
            requirements = {}
            if form.branchRequirements.data != "":
                requirements = json.loads(form.branchRequirements.data)
            requirements['_id'] = id
            requirements['name'] = form.name.data
            requirements['location'] = form.location.data
            requirements['contact'] = form.contact.data
            requests.put(urlput, json=requirements)
            return redirect(url_for('home'))
    elif 'delete' in request.form:
        deleteAction(branchid)
        flash('Successfully Deleted', 'success')
        return redirect(url_for('home'))
    else:
        requirements = {}
        for requirement in branch:
            requirements[requirement] = branch[requirement]

        form.name.data = requirements['name']
        del requirements['name']
        form.location.data = requirements['location']
        del requirements['location']
        form.contact.data = requirements['contact']
        del requirements['contact']
        del requirements['_id']
        if requirements:
            form.branchRequirements.data = json.dumps(requirements)
        else:
            form.branchRequirements.data = ''

        if 'editBranch' in request.form:
            return render_template("update.html", form=form, requirements=requirements, edit="true", authenticated=isAuthenticated)

    return render_template("update.html", form=form, requirements=requirements, edit="false", authenticated=isAuthenticated)


def deleteAction(branchid):
    urldelete = url+"/requirement?_Id={}".format(branchid)
    requests.delete(urldelete)


if __name__ == "__main__":
    app.run(debug=True)
