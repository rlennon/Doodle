# GitHub

- [GitHub](#github)
  - [Setup](#setup)
  - [Strategy](#strategy)

## Setup
The GitHub [repository](https://github.com/rlennon/Doodle) was created by the PO.

Each member of the team was given access to the repository.

To keep things simple and follow best practices we tried to align with GitHub conventions wherever possible.

## Strategy

We have adopted a simple branching strategy based on trunk based development, all code and documentation is held within the master branch. This involves:

- Each engineer having a copy of the code on their own local machine.

- Each engineer makes changes locally.

- Those changes are then pushed to the GitHub repository.

- Within Github a pull request is created and all members of the team should be assigned as reviwers of the pull request.

- The team members assigned as reviewers will all receive notification within Slack of the pull request and can review those changes.

- Originally 2 teams members had to peer review each pull request but this was reduced to 1 after a discussion amoungst the team.

- If the changes are acceptable then the team member who reviewed them puts in a comment & clicks approve. If the changes are not acceptable then the team member puts in a comment and rejects the pull request so it goes back to the original engineer for updates.

- When the pull request has been approved, anyone in the team can go into the pull request and merge the commit which moves the code into the master branch. The branch that was uploaded as part of the pull request can then be deleted as a housekeeping task.

- When code is committed to the master branch a Jenkins build job will run automatically which pulls all the code from GitHub, runs it through nose tests, tars up the code into a package then uploads the package to Artifactory.

- Then a Jenkins deploy job runs which pulls the package from Artifactory and deploys the code to the Stage environment and then deploys it to the Production environment.