# Doodle

M.Sc. DevOps Team 1

# Table of Contents

- [Doodle](#doodle)
- [Table of Contents](#table-of-contents)
  - [Introduction!](#introduction)
    - [Product Owner](#product-owner)
    - [Rockstars](#rockstars)
  - [Project Deadline](#project-deadline)
  - [Project Specification](#project-specification)
  - [Considerations](#considerations)
  - [Useful Links](#useful-links)
    - [For more information visit our other sections](#for-more-information-visit-our-other-sections)
  - [Risk Register](#risk-register)
  - [Tenants of Design](#tenants-of-design)
  - [Social Contract](#social-contract)

## Introduction!

This is the online repository for the engineering and tech giant **Doodle**. Our current product **Brancher** will be delivered using an Agile methodology that embraces the [DevOps culture](https://martinfowler.com/bliki/DevOpsCulture.html). 
Please note that our culture embraces change and these documents are treated as living, breathing artefacts that will be continuously updated.

### Product Owner

Ruth G. Lennon

### Rockstars

Colin, Conor, Emmet, Fiona, Francis, Lee, Peter, Wes

## Project Deadline

5th May 2019 at 23:59

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

## Considerations

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
| [Project Log](./content/projectlog.md) | Log of project activities |
| [Costings](./content/costings.md) | Overview of the project cost |
| [Architecture](./content/architecture.md) | Outlines the architecture |
| [Environments](./content/environment.md) | Overview of the environment set-up |
| [Requirements](./content/requirements.md) | Overview of the requirements for the project |

## Risk Register

These are the current Risks on the project, re-aligned on a weekly basis

- Infrastructure proving to be a real problem, may block being able to release software
- Team is finding itself to be running short on time due to other work and study commitments
- No working software in production yet
- Unknown technology choices has led to a lot of upskilling required
- Changing / ambiguous requirements
- Talk of the company being bought out has raised concerns
- Lack of rights for toolsets chosen has hindered progress and ability to deliver

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

## Social Contract
**Meetings**

- Stand-ups will occur straight after class on Monday night & Friday morning, even on Bank Holidays.
- The order that people give their updates will be based on alphabetical order of those present at the meeting.
- Updates will be in the form: What I've done, What I plan to do, Impediments
- Sprint planning will occur every Thursday at 8pm GMT.
- Please add and update items within Jira prior to the sprint planning session.
- Sprint retro will occur every second week, at the start of the sprint planning meeting.
- The order that people present their sprint retro updates will be based on alphabetical order of those present at the meeting.
- Points raised in the sprint retro will be noted and posted on the Doodle slack retro channel by the Scrum Master.
- Backlog refinement?
- Task estimation will be done using Planning Poker with Slack
- Come prepared to meetings.
- Be on time for Stand Ups and meetings.
- Mobile phones on silent.
- Everyone has equal voice and valuable contribution.
- Keep your language and tone professional at all times.
- Be honest.

**Communication**

- Slack is the preferred method of communication.
- If a demonstration is required use Zoom, record the session and upload to the Slack channel.
- No Slack communications between midnight and 7am GMT.
- Raise a problem as soon as you see it.
- Respect each other and understand differences in knowledge.
- All team documents are to be created using Markdown language and shared on GitHub.
- There are no silly questions, if you don’t understand, ask.
- Share success stories.
- Focus on the positives.
- Don’t make assumptions.
- Don’t interrupt and cut another person off while they are talking.
- Listen when someone is talking, don’t interject.
- Zero tolerance for bullying.
- Communication in this order: Slack, Zoom, Blackboard.
- Agile way of working.
- If are assigned a job, take ownership of it and keep it up to date.
- Stick to your agreed working patterns. Let the team know when you are late or going early.
- Keep JIRA board updated at all times.
- Update the Scrum Board as you progress the story i.e. don’t update at standup.
- Don't be afraid to ask for help.
- Don't be afraid to give constructive critism, as long as it is constructive.
- Solve roadblocks within the team. If the impediment can’t be solved within the team then give it to the Scrum Master.

**Other**
- Sprints will start Friday morning at 9am EST and run for 1 week
- The Scrum Master role rotates each week, the schedule will be kept within the Process page on GitHub (https://github.com/rlennon/Doodle/blob/master/content/process.md)
- Jira will be used for task management and planning.
- Each member of the team will work 6 hours per week, unless they are on vacation.


**Estimating Story Points Within Jira**

1 = Up to 1 day to complete

2 = From 1 day to 2.5 days to complete

5 = From 2.5 to 1 week to complete

8 = From 1 week to 2 weeks to complete (needs to be broken into at least 2 stories)

13 = Multiple weeks to complete (needs to be broken into at least 3 stories)

