# Security



One tool we used for securing the project is SonarQube.

SonarQube is a code quality tool i.e. it checks code for bugs and security vulnerabilities. The results of those checks can be monitored on a dashboard visable on the SonarQube server. The team decided to use SonarQube due to a number of the team being familiar with it from previous projects and it being the de-facto tool for  code analysis.

To get Sonarqube setup we first needed to create a Ubuntu server, we gave the server 1 CPU, 4GB of memory & 50GB of storage.

When Ubuntu was installed we installed Java 1.8 as Java is needed for SonarQube.

Then we carried out the SonarQube perquisites, this involved following the procedure at https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-in-ubuntu-16-04 to:

 - Install Nginx

 - Install MySQL which included security hardening

 - Install PHP for Processing which included security hardening

 - Configure Nginx to use the PHP Processor

When that was done were were able to install SonarQube by following the procedure at https://www.digitalocean.com/community/tutorials/how-to-ensure-code-quality-with-sonarqube-on-ubuntu-16-04 which involved:

 - Preparing for the install which included creating a sonarqube user

 - Downloading and installing SonarQube

 - Configuring the SonarQube Server

 - Configuring the Reverse Proxy

 - Securing SonarQube

 - Setting up the Code Scanner on the Jenkins server 

 - Running a test scan

SonarQube automatically creates an admin user when installed so within the SonarQube console I created a normal user called Doodle which can be used to view scan results.

Within Jenkins we set up connectivity with the SonarQube server by adding the SonarQube server details under the Manage Jenkins -> Configure System page. We also added settings for SONARQUBE_SERVER and SONARQUBE_PORT variables which we use within the Jenkins job.

Then we added the following to the build Jenkinsfile so the SonarQube job would run after the Nosetests ran but before the code was tarred and loaded to Artifactory:

**stage('Static Code Analysis') {
  	steps {
	  sh '''
			echo "*************************Static Code Analysis*************************"
			sh /usr/local/bin/sonar-scanner -Dsonar.host.url=${SONARQUBE_SERVER}:${SONARQUBE_PORT} -Dsonar.login=************************************************** **-Dsonar.projectName=Doodle -Dsonar.projectKey=DoodleTest -Dsonar.sources=${WORKSPACE}/src
		  '''
	 	}	
	 }**

When this code was committed to the master branch an automatic Jenkins build and deploy ran which created the SonarQube job and then ran the SonarQube job as part of the pipeline which analysed the code within the branch and produced a report on the SonarQube dashboard showing the code quality.

SonarQube can be set to fail the Jenkins pipeline if a certain level of code quality isn't reached. We currently don't have SonarQube set up to fail but this would need to be a future enhancement that the team would carry out as it's standard practice within software development. 