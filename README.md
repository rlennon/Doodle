# Doodle

M.Sc. DevOps Team 1

# Introduction

This project is a webservice for the "Doodle" tech company. This project will be delivered using DevOps/agile methodology

//TODO: Build/Release badges go here

# Project Specification

- "Requirements gathering" on-line system to store building project requirments
- Clean and simple design
- Document (jpg) handling (upload/viewing )
- User access levels (client, administrator)
- Includes at lease one self developed api and one webservice 

The customer would like an on-line system to enter details for the latest Doodle branch. Doodle is a
engineering and tech company. Their most popular product is a browser. The system must take details
of their requirements to ensure that all needs of the branch are listed for a building contractor. For
example, they may wish to have a 538,000 square feet building for the data center. It may need to be
held underwater. The requirements gathering system should be clean and simple. The system needs
to take into account the usual details about dimensions and cost/budget. It must be possible to upload
files or images which may be sample construction diagrams. Jpgs are fine. Do not worry about autocad,
etc. The administrator should be able to access detailed information and edit as appropriate. Once
the client enters details it should not be able to be changed by the client.

# Team

Colin, Conor, Emmet, Fiona, Francis, Lee, Peter, Wes

# Ceremonies

 - Sprint Duration: 1 week
 - Planning : Thursdays 8pm
 - Standups: Monday / Friday after class
 - Demos: Recorded after each sprint and shared
 - Retrospectives: Thursdays before planning

# Definition of Done

//TODO

# Links

- Slack: https://lyit.slack.com/messages/GGGLUP8H3
- Jira: 
- GitHub: https://github.com/rlennon/Doodle

# Technology

- Language: Python
- Datastore: Mongo

# Architecture

//TODO

# Risk Register

//TODO

# Tenants of Design

- dedication to clean, secure, performant and self documented code
  - code Frameworks used
  - code coverage tool used
  - Secure code: Regex for cleansing and validation, Named queries and database triggers
  - performance testing tool to be used
- documentation/ code commenting (javadoc)/seperate branch
- Database for persistant storage
- testing:
  - Unit testing
  - integretation testing
  - UA
 - Environments:
    - staging and production
    - tight configuration management for consistency and reproducibility
    - automated creation and deployments
 - integrated and automated pipeline (commit -> test -> deploy)
 - github version control:
  - branches used
  - version/release management
 - agile project management methods/principles (jira)
