# Jenkins VM setup instructions with Python Virtual Environment

The following instructions are for setting up a new VM with Ubuntu. After this setup, Jenkins will be able to pull from the repository, setup up a python virtual environment, install all required python modules to run unit tests and pytlint (python modules can be added to src/pipelines/build/requirements.txt). The python virtual environment is rebuilt on every build, and is isolated from the system.

## VM

To be run on a clean Ubuntu install:

1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo apt-get install git-core
4. sudo apt-get install default-jdk

### Install Jenkins

1. sudo wget --no-check-certificate -qO - http://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add –

2. sudo echo deb http://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list

3. sudo apt-get update
4. sudo apt-get install –y jenkins

## Start & Unlock Jenkins

1. sudo systemctl start jenkins
2. sudo vi /var/lib/jenkins/secrets/initialAdminPassword

### Config Jenkins

1. Install Suggested Plugins

## Add key to Jenkins & Github

1. sudo su - jenkins
2. mkdir ./.ssh
3. cd .ssh
4. ssh-keygen -t rsa -C "jenkins@CI"
5. eval "$(ssh-agent -s)"
6. ssh-add id_rsa
7. cat id_rsa.pub

8. *Add the above key to github

9. ssh -T git@github.com

## Setup Python Virtual Environment

1. Exit jenkins user (su - username)
2. sudo apt install python-pip
3. sudo pip install --upgrade pip
4. sudo pip install virtualenv
5. sudo /usr/bin/easy_install virtualenv
6. cd /usr/local/bin
7. sudo chown jenkins virtualenv

## Create Jenkins Pipeline

Note: The following instructions are for testing only. Changes to the actual jenkins build file will require an RFC.

1. Add new pipeline
2. General
    * Check 'Github Project'
    * Add URL to github project
3. Build Trigger
    * Enter required build trigger (ie Poll SCM - H/15 * * * * )
4. Pipeline
    * Definition - Pipeline script from SCM
    * SCM - Git
    * Repository URL - Copy SSH from git hub (ie git@github.com:User/repository)
    * Script Path - Jenkinsfile
5. Save