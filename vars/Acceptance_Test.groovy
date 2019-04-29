#!/usr/bin/env groovy

def call(String STAGING_ENDPOINT = 'test') {
    sh '''
        echo "*************************Testing connection to the Endpoint*************************"
        if curl -v ${STAGING_ENDPOINT} 2>&1 | grep "HTTP/1.1 200 OK"
        then
	        echo "Deployment Successful!"
          else
	          echo "Endpoint Test not successful, please investigate!"
	          exit 1
          fi
      '''
}