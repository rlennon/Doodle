//Just a wee example for Artifactory
//link to help understand Artifactory = https://www.jfrog.com/confluence/display/RTF/Working+With+Pipeline+Jobs+in+Jenkins
//This code is downloading conord-1.0.0.jar file from artifactory

stage('artifactory'){
    steps{
        script{
            def server = Artifactory.server'art'  //##art1 is a global config
            def rtGradle = Artifactory.newGradleBuild() //##create gradle build
            rtGradle.resolver server:server,repo:'smrtwo-dev' //##download Dependancies from smrtwo-dev

            def artfDownload = """{
                "files":[
                    {
                        "pattern":"smrtwo-dev/first/conord/1.0.0/Conord-1.0.0.jar",
                        "target":"smrtwo-dev/"
                    }
                ]
            }"""
            server.download(artfDownload)

            def build = server.download artfDownload
            server.publishBuildInfo build
        }
    }
}