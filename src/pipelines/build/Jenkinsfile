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
    			  extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: "rlennon/doodle/src/POC/PythonAPI"]], 
    			  submoduleCfg: [], 
   			    userRemoteConfigs: [[url: 'git@github.com:rlennon/doodle']]
    		  ])
			  }
		  }	
	  }
  	stage('Code Coverage Testing - Python Builder') {
  		steps {
			 sh '''
			 			echo "*************************Running Nosetests with Python Builder*************************"
						cd ${WORKSPACE}/rlennon/doodle/src/POC/PythonAPI/src/POC
			 			sudo nosetests3 --with-coverage --cover-package=PythonAPI
					'''
		  }	
	  }
		stage('Build/Tar Package') {
	  	steps {
		  sh '''
						echo "*************************Build/Tar Package*************************"
						tar -cvf doodle_build-${BUILD_NUMBER}.tar ${WORKSPACE}/rlennon/doodle/src/POC/PythonAPI/src/POC/PythonAPI/*
						ls -ltr
				  '''
	  	}	
	  }
  	stage('Artifactory Load') {
  		steps {
			sh '''
					echo "*************************Artifactory Load*************************"
					echo "curl command pushes new build package into artifactory"
					curl -u ${ARTIFACTORY_USER}:${ARTIFACTORY_PASSWORD} -X PUT "http://172.28.25.122:8081/artifactory/doodle-release-local/com/doodle/build/doodle_build-${BUILD_NUMBER}/doodle_build-${BUILD_NUMBER}.tar" -T ${WORKSPACE}/doodle_build-${BUILD_NUMBER}.tar
		  		rm ${WORKSPACE}/doodle_build-${BUILD_NUMBER}.tar
				'''
		}	
	  }
  }
	post {
		always {
			cleanWs()
		}
	}
}