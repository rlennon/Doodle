from flask import Flask, render_template, url_for, flash, redirect, request

import os
import Forms
import json
import requests


app = Flask(__name__)

app.config['SECRET_KEY'] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'

if 'DOODLE_CONFIG' in os.environ:
    filepath = os.environ['DOODLE_CONFIG']
else:
    filepath = '../dev_config.json'

with open(filepath) as f:
    config = json.load(f)

hostIp = config.get("hostIp")
port = config.get("apiPort")
url = "http://{}:{}".format(hostIp, port)

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
                'contact': doc['contact']
            }
        )
    return render_template("home.html", branches=branches)

@app.route("/create/", methods=['GET', 'POST'])
def create():
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


@app.route("/branch/<branchid>", methods=['GET', 'POST'])
def update(branchid):
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
            return render_template("update.html", form=form, requirements=requirements, edit="true")
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
            return render_template("update.html", form=form, requirements=requirements, edit="true")

    return render_template("update.html", form=form, requirements=requirements, edit="false")


def deleteAction(branchid):
    urldelete = url+"/requirement?_Id={}".format(branchid)
    requests.delete(urldelete)


if __name__ == "__main__":
    app.run(debug=True)
