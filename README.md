# Doodle

M.Sc. DevOps Team 1

# Table of Contents

- [Doodle](#doodle)
- [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Rockstars](#rockstars)
  - [Project Specification](#project-specification)
  - [Considerations](#Considerations)
  - [Useful Links](#useful-links)
    - [For more information visit our other sections](#for-more-information-visit-our-other-sections)
  - [Risk Register](#risk-register)
  - [Tenants of Design](#tenants-of-design)

## Introduction!

This is the online repository for the engineering and tech giant **Doodle**. Our current product **Brancher** will be delivered using an Agile methodology that embraces the [DevOps culture](https://martinfowler.com/bliki/DevOpsCulture.html). 
Please note that our culture embraces change and these documents are treated as living, breathing artefacts that will be continuously updated.

### Rockstars

Colin, Conor, Emmet, Fiona, Francis, Lee, Peter, Wes

## Project Specification

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

## Considerations:

- Frameworks
- Database
- Database persistence technology 
- Define the buisness Requirements
- Named queries and database triggers for security 
- Regex for cleansing and validation of data before sending to the database.

## Useful Links

- Slack: https://lyit.slack.com/messages/GGGLUP8H3
- Jira: https://studentjira.lyit.ie/secure/RapidBoard.jspa?projectKey=DOODLE&rapidView=51&view=planning.nodetail
- GitHub: https://github.com/rlennon/Doodle

### For more information visit our other sections

| Section  | Description  |
|---|---|
| [Process](./content/process.md) | Describes the companies process  |
| [Architecture](./content/architecture.md) | Outlines the architecture |
| [Environments](./content/environment.md) | Overview of the environment set-up |
| [Requirements](./content/requirements.md) | Overview of the requirements for the project |

## Risk Register

Please see our list of Risks

//TODO: Embed query here?

## Tenants of Design

- Dedication to clean, secure, performant and self documented code
  - code Frameworks used
  - code coverage tool used
  - Secure code: Regex for cleansing and validation, Named queries and database triggers
  - performance testing tool to be used
- Documentation / code commenting (javadoc)/seperate branch
- Datastore for persistance
- Testing:
  - Unit testing
  - integretation testing
  - UA
- Environments:
  - staging and production
  - tight configuration management for consistency and reproducibility
  - automated creation and deployments
  - integrated and automated pipeline (commit -> test -> deploy)
- Github version control:
  - branches used
  - version/release management
- Agile project management methods/principles (jira)