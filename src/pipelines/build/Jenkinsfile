pipeline {
  agent any
  stages {
    stage('GitHub Pull') {
	  	steps {
		  	sh 'echo "*************************GitHub Pull*************************"'
				script {
					    scm_checkout.SCM_checkout(src/POC)
				}
			}	
	  }
  	stage('Sonar Testing') {
  		steps {
			  sh 'echo "*************************Sonar Testing*************************"'
 		  }	
	  }
				stage('Build/Tar Package') {
	  	steps {
		  	sh 'echo "*************************Build/Tar Package*************************"'
				sh 'tar -cvf doodle_build-${BUILD_NUMBER}.tar ${WORKSPACE}/src/POC/*'
		  }	
	  }
  	stage('Artifactory Load') {
  		steps {
			  sh 'echo "*************************Artifactory Load*************************"'
 		  }	
	  }
  }
}
