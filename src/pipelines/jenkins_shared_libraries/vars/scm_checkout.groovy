#!/usr/bin/env groovy

def SCM_checkout(${SCM_Dir}) {
  checkout([$class: 'GitSCM', 
    branches: [[name: '*/master']], 
    doGenerateSubmoduleConfigurations: false, 
    extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: "rlennon/doodle/${SCM_Dir}"]], 
    submoduleCfg: [], 
    userRemoteConfigs: [[url: 'git@github.com:rlennon/doodle']]
    ])
}