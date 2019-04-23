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
    			  extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: "rlennon/doodle/src"]], 
    			  submoduleCfg: [], 
   			    userRemoteConfigs: [[url: 'git@github.com:rlennon/doodle']]
    		  ])
			  }
		  }	
	  }
	stage('Package Prep') {
	 	steps {
		  	sh '''
			  	echo "*************************Staging package*************************"
				cd ${WORKSPACE}
				mkdir package
				cd ${WORKSPACE}/rlennon/doodle/src/src
				mv services ${WORKSPACE}/package
				mv ui ${WORKSPACE}/package
				mv requirements.txt ${WORKSPACE}/package
				mv config.json ${WORKSPACE}/package
				cd ${WORKSPACE}/package
				ls -ltr
			'''
  		}	
	}
  	stage('Code Coverage Testing - Python Builder') {
  		steps {
			 sh '''
			 			echo "*************************Running Nosetests with Python Builder*************************"
						if [ -n "${WORKSPACE:+1}" ]; then
    						  # Path to virtualenv cmd installed by pip
    						  # /usr/local/bin/virtualenv
    						  PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
    						  if [ ! -d "venv" ]; then
            					    virtualenv -p python3 venv
    						  fi
    						  . venv/bin/activate
						fi
						pip install -r ${WORKSPACE}/rlennon/doodle/src/src/pipelines/build/requirements.txt 
						cd ${WORKSPACE}/package
						nosetests --with-coverage --cover-package=services
						pylint --disable=C0103 services/api.py || exit 0
					'''
		  }	
	  }
	stage('Build/Tar Package') {
	  	steps {
		  sh '''
						echo "*************************Build/Tar Package*************************"
						cd ${WORKSPACE}
						tar -cvf doodle_build-${BUILD_NUMBER}.tar ${WORKSPACE}/package/*
						ls -ltr
				  '''
	  	}	
	  }
  	stage('Artifactory Load') {
  		steps {
			sh '''
					echo "*************************Artifactory Load*************************"
					echo "curl command pushes new build package into artifactory"
					curl -u ${ARTIFACTORY_USER}:${ARTIFACTORY_PASSWORD} -X PUT "${ARTIFACTORY_SERVER}:${ARTIFACTORY_PORT}/artifactory/doodle-release-local/com/doodle/build/doodle_build-${BUILD_NUMBER}/doodle_build-${BUILD_NUMBER}.tar" -T ${WORKSPACE}/doodle_build-${BUILD_NUMBER}.tar
		  		    rm ${WORKSPACE}/doodle_build-${BUILD_NUMBER}.tar
				'''
		}	
	  }
  }
	post {
		success {
			build job: 'Doodle_Deploy_Staging', parameters: [string(name: 'DOODLE_BUILD_JOB_BUILD_NUMBER', value: "${BUILD_NUMBER}")]
		}	
		always {
			cleanWs() 
		}
	}
}