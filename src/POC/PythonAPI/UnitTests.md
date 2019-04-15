# Doodle Python API Unit Tests

## Jenkins Server Requirements

### Python3.6

The python environment on the Jenkins server must have installed, in addition to the required modules for the api:

* nose

Nose will run all files that are prefixed with 'test_'

### Jenkins

Jenkins requires the following plugins:

* Python Plugin
* ShiningPanda Plugin

## Setup Jenkins Job

1. Add build step - Python Builder
2. Python version should be Python3.6 (This can be changed in Manage Jenkins - Global Tool Configuration)
3. Nature: Shell
4. Command: nosetests --with-coverage --cover-erase --cover-package=PythonAPI --cover-html /var/lib/jenkins/workspace/Doodle/src/POC/PythonAPI (replace with path to workspace if different)
