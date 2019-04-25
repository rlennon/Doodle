# Unit Testing

* [Unit Testing](#unit-testing)
  * [Local Development Environment](#local-development-environment)
    * [Setup](#setup)
      * [Python](#Python)
      * [Modules](#Modules)
    * [FAQ / KB](#faq--kb)
      * [Python Unit Tests](#Python-Unit-Tests)
      * [Structure](#Structure)
      * [Unit Test File Naming](#Unit-Test-File-Naming)
      * [Coverage](#Coverage)
  * [Hosted Environment](#hosted-environment)
    * [Setup](#setup-1)
      * [Python Environment](#Python-Environment)
      * [requirements.txt](#requirements.txt)
      * [Jenkins File](#Jenkins-File)
    * [FAQ / KB](#faq--kb-1)
      * [Fail Threshold](#Fail-Threshold)

## Local Development Environment

### Setup

#### Python

* Python 3.6

#### Modules

* A list of required modules are stored in scm
  * For Production [here](../src/requirements.txt)
  * For Build (including the unit test modules) [here](../src/pipelines/build/requirements.txt)

### FAQ / KB

#### Python Unit Tests

* Written using unittest
* By default, unittest only runs functions whose name starts with `test`
* unittest can be run using nosetest from the command line using `nosetests --with-coverage --cover-package=services`

#### Structure

Unit tests should be inside a folder named 'UnitTests' in the same folder as the package to be tested.

#### Unit Test File Naming

> nose collects tests automatically from python source files, directories and packages found in its working directory (which defaults to the current working directory). Any python source file, directory or package that matches the testMatch regular expression (by default: (?:^|[b_.-])[Tt]est) will be collected as a test (or source for collection of tests).
<cite>[nose documentation](https://nose.readthedocs.io/en/latest/usage.html#extended-usage)</cite>

#### Coverage

Unit test have been written for:

* Services
  * [api.py](../src/services/api.py)
    * Unit Test Files
      * [test_Requirement.py](../src/services/Unittests/test_Requirement.py) - Requirement endpoint
      * [test_Requirementlist.py](../src/services/Unittests/test_Requirementlist.py)  - RequirementList endpoint
    * Notes
      * Mock is used to patch the pymongodb and web service calls
  Test split between 2 files (by end point)

## Hosted Environment

### Setup

#### Python Environment

A virtual python environment is required during the jenkins build to enable the tests to run.

* Virtual Environment
  * Set up
    * Environment set up using virtualenv
    * virtualenv set up [here](./jenkinsvirtualenv.md)

#### requirements.txt

* Separate requirements.txt for testing (including the additional required modules)
  * For Build (including the unit test modules) Located [here](../src/pipelines/build/requirements.txt)

#### Jenkins File

* nosetests is used to run the unit tests
* The JenkinsFile is configured to run nosetests on the services package (folder)
* Jenkins Coverage
  * Services package
    * [api.py](../src/services/api.py)
* The Jenkins build file is located [here](../src/pipelines/build/Jenkinsfile). Changes to the jenkins file requires an RFC.
* Jenkinsfile contains the command to create the Python Virtual Environment.
* The command to run nosetests : `nosetests --with-coverage --cover-package=services`

### FAQ / KB

#### Fail Threshold

* Currently, there is no fail threshold for the build job (all results will pass)