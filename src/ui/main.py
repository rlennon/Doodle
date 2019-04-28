import os
import Forms
import json
import requests
import base64
import datetime
from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)

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


def authCheck(session_key):
    session_url = url + "/session?_Id={}".format(session_key)
    response = requests.get(session_url)
    session = response.json()
    if "_id" in session:
        now = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
        tdelta = datetime.datetime.strptime(session["login_date"], "%m-%d-%Y-%H-%M-%S") -\
            datetime.datetime.strptime(now, "%m-%d-%Y-%H-%M-%S")
        print("Login_date:{}".format(session["login_date"]))
        print("now:{}".format(now))
        print(tdelta.seconds)
        if tdelta.total_seconds()/60 > 900:
            return False, False
        elif session["uname"] == "admin":
            isAdmin = True
            isAuthenticated = True
            return isAuthenticated, isAdmin
        else:
            return True, False

    else:
        return False, False




@app.route("/")
@app.route("/home")
@app.route("/home/")
@app.route("/create")
@app.route("/create/")
def reroute():
    return redirect(url_for('login'))


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = Forms.LoginForm()
    if form.validate_on_submit():
        if form.username.data in logins and logins[form.username.data].decode("utf-8") == form.password.data:
            session_data = {}
            now = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
            session_data["login_date"] = now
            session_data["uname"] = form.username.data
            urlpost = url + "/session"
            response = requests.post(urlpost, json=session_data)
            col = response.json()
            session_key = col["$oid"]
            flash('Successfully Logged in', 'success')
            return redirect(url_for('home', session_key=session_key))
        else:
            flash('Incorrect Details', 'danger')
            return redirect(url_for('login'))

    return render_template("login.html", form=form)


@app.route("/home/<session_key>", methods=['GET', 'POST'])
def home(session_key):
    isAuthenticated, isAdmin = authCheck(session_key)
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
    return render_template("home.html", branches=branches, authenticated=isAuthenticated, session_key=session_key,
                           admin=isAdmin)

@app.route("/create/<session_key>", methods=['GET', 'POST'])
def create(session_key):
    isAuthenticated, isAdmin = authCheck(session_key)
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
            return render_template("create.html", form=form, requirements=requirements, authenticated=isAuthenticated, session_key=session_key, admin=isAdmin)
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
            return redirect(url_for('home', session_key=session_key))

    return render_template("create.html", form=form, requirements=requirements, authenticated=isAuthenticated, session_key=session_key, admin=isAdmin)


@app.route("/branch/<session_key>/<branchid>", methods=['GET', 'POST'])
def update(session_key, branchid):
    isAuthenticated, isAdmin = authCheck(session_key)
    if isAuthenticated is False:
        flash('Please Login', 'danger')
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
            return render_template("update.html", form=form, requirements=requirements, edit="true", authenticated=isAuthenticated, session_key=session_key, admin=isAdmin)
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
            return redirect(url_for('home', session_key=session_key))
    elif 'delete' in request.form:
        deleteAction(branchid)
        flash('Successfully Deleted', 'success')
        return redirect(url_for('home', session_key=session_key))
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
            return render_template("update.html", form=form, requirements=requirements, edit="true",
                                   authenticated=isAuthenticated, session_key=session_key, admin=isAdmin)

    return render_template("update.html", form=form, requirements=requirements, edit="false",
                           authenticated=isAuthenticated, session_key=session_key, admin=isAdmin)


def deleteAction(branchid):
    urldelete = url+"/requirement?_Id={}".format(branchid)
    requests.delete(urldelete)


if __name__ == "__main__":
    app.run(debug=True)
