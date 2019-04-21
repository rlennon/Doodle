#!/usr/bin/env groovy

pipelines.jenkins_shared_libraries.vars

def SCM_checkout(SCM_Dir) {
  checkout([$class: 'GitSCM', 
    branches: [[name: '*/master']], 
    doGenerateSubmoduleConfigurations: false, 
    extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: "rlennon/doodle/${SCM_Dir}"]], 
    submoduleCfg: [], 
    userRemoteConfigs: [[url: 'git@github.com:rlennon/doodle']]
    ])
}