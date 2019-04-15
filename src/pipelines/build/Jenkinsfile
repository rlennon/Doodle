pipeline {
  agent any
  stages {
    stage('GitHub Pull') {
	  	steps {
		  	sh 'echo "*************************GitHub Pull*************************"'
			script {
				checkout([$class: 'GitSCM', 
   		   	branches: [[name: '*/master']], 
    			doGenerateSubmoduleConfigurations: false, 
    			extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: "rlennon/doodle/src/services"]], 
    			submoduleCfg: [], 
   			 userRemoteConfigs: [[url: 'git@github.com:rlennon/doodle']]
    		])
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
			sh 'tar -cvf doodle_build-${BUILD_NUMBER}.tar ${WORKSPACE}/rlennon/doodle/src/services/src/services/*'
			sh 'ls -ltr'
		}	
	  }
  	stage('Artifactory Load') {
  		steps {
			sh 'echo "*************************Artifactory Load*************************"'
			sh 'echo "curl command pushes new build package into artifactory"'
			sh 'curl -u ${ARTIFACTORY_USER}:${ARTIFACTORY_PASSWORD} -X PUT "http://172.28.25.122:8081/artifactory/doodle-release-local/com/doodle/build/doodle_build-${BUILD_NUMBER}/doodle_build-${BUILD_NUMBER}.tar" -T ${WORKSPACE}/doodle_build-${BUILD_NUMBER}.tar'
		  }	
	  }
  }
}
