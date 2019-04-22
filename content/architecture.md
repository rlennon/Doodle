# Architecture

Here we outline not only our current architecture but the journey taken to get there.

# Table of Contents

- [Architecture](#architecture)
- [Table of Contents](#table-of-contents)
  - [Process Architecture](#process-architecture)
  - [Technology Choices](#technology-choices)
  - [Application Artitecture](#application-artitecture)
  - [Software](#software)

## Process Architecture

<img src="./images/arch_v1.jpg" alt="version 1" width="1100"/>

## Technology Choices

- Language: Python
- webservices: Flask+gnuicorn
- Datastore: Mongo
- Version Control : GitHub
- Issue tracking : JIRA
- CI : Jenkins
- Binary Managemnet : Artifactory

## Application Artitecture

<img src="./images/app_arch_v1.png" alt="version 1" width="1100"/>

The application will reside on 2 VMs within the LYIT-CDC datacenter.

- VM1 hosts the frontend webservice. The webservice consists of python flask application wrapped in gnuicorn webserver.
- VM2 hosts API. The API consists of python flask application wrapped in gnuicorn webserver connecting to local mongodb.

## Software

| Software | Version | Reason For Choosing Software |
|---|---|---|
| Ubuntu | 16.04 |  |
| Mongo | 4.0.6   |  |
| Python |  3.5  |  |
| Artifactory |    |  |
| Terraform |  0.11.13  |  |
| Jenkins |  2.164.1  |  |
| Git | 2.7.4   |  |
| Vagrant |  2.2.4  |  |
| Virtualbox | 6.0.4 |  |
| Ansible |  2.7.10  |  |


## Jenkins Installation And Configuration

[Jenkins Installation And Configuration](./jenkins.md)

## Artifactory setup

* Ask for login for ubuntu and artifactory, not putting it on github.

* Once in ubuntu go to terminal and log in as root. -> sudo su

* Once in root go to. -> cd /opt/jfrog/artifactory-oss-6.9.1/bin

* Run. -> ./installService.sh

* Once in bin, type systemctl start artifactory.service

* Artifactory should start up. Then look for youre ip address by typing. -> ip addr show

* use ip address with 8081 and put the following in a browser,example -> 172.28.25.118:8081

* When you see artifactory you should type in the username and password, which will be given if asked.

* To stop Artifactory. -> systemctl stop artifactory.service
