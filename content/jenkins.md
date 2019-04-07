We created the Jenkins Dev server, called Doodle-Jenkins-Dev, and installed ubuntu 16.04 on it.

We installed Java 1.8 by running the following commands:

**sudo add-apt-repository ppa:webupd8team/java**

**sudo apt update; sudo apt install oracle-java8-installer**

**sudo apt install oracle-java8-set-default**

We followed the procedure in Jenkins_2018_Part_1.pdf to install Jenkins on the Jenkins Dev server:

**wget --no-check-certificate -qO - https://pkg.jenkins.io/debian/jenkins-ci.org.key - sudo apt-key add -**

**sudo echo deb http://pkg.jekins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list**

**sudo apt-get update**

**sudo apt-get install jenkins**

**sudo systemctl start jenkins**

**sudo systemctl status jenkins**

We unlocked Jenkins by connecting to **127.0.0.1:8080** & following the instructions to unlock Jeknins.

We installed the suggested plugins.

The Jenkins Admin account was set up as Jenkins.

We installed the following plugins:

**JaCoCo, Ansible, Slack Notification, Javadoc, Maven Integration, Config File Provider, Ivy, Artifactory, Log Parser, Icon Shim, GitHub Integration, Build With Parameters, GitHub Authentication, WMI Windows Agents, External Monitor Job Type, Powershell, SonarCube Scanner, Groovy, GitHub Pull Request Coverage Status, mongodb-document-upload.**

Putty was installed on the Ubuntu server

**sudo apt-get -y install putty**

**sudo apt-get -y install putty-tools**

Git was installed on the Ubuntu server

**sudo apt-get -y install git**

We setup Jekins to connect to GitHub:

**cd**

**mkdir ./.ssh**

**ssh-keygen –t rsa –C “jenkinsCI”**

**eval “$(ssh-agent –s)”**

**ssh-add id_rsa**

Display the content of the key:

**cat id_rsa.pub**

Now add this key to GitHub by opening GitHub in the browser and logging in.
 
Under the users icon select **Settings**.

From the menu on the left select **SSH & PGP Keys**.

Select the **New SSH Key** button.

Select the key from the CLI.

Right click and select copy.

Paste it into the browser in the window.

This key can now be seen stored by GitHub.

Go back to the virtual machine & type in:

**ssh -T git@github.com**

You should now get a successful authentication message which shows it's working.