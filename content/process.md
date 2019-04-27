# Process

This page will outline the various processes that we have refined as the project progressed, focusing on both the technical and non-technical sides.

## Non-Tech

### Scrum

For the most part we follow traditional SCRUM, due to the timelines applied to us we are unable to have daily stand-ups so we have two per sprint, our sprints are also only 1 week in duration. 

#### Team Breakdown

Being a forward thinking company, we like to keep our people both happy and challenged, this means we change roles **A LOT!**

| Role | Week 0 1/3 | Week 1 8/3 | Week 2 15/3 | Week 3 22/3 | Week 4 29/3 | Week 5 5/4 | Week 6 12/4 | Week 7 19/4 |
|---|---|---|---|---|---|---|---|---|
| **Scrum Master** | Francis | Colin | Conor  | Emmet   | Fiona | Lee | Peter   | Wes |
| **Proxy PO**     | Conor   | Emmet | Fiona  | Lee     | Peter | Wes | Francis | Colin |
| **Tech Lead**    | Emmet   | Fiona | Lee    | Peter   | Wes   | Francis | Colin | Conor |

#### Defined Roles

A Scrum Master within the Doodle group has the following roles & responsibilities:

- Setting up any meetings that are required.
- Attempts to resolve impediments that the team may have, though it would be better if the team were able to resolve impediments themselves.
- Works with the PO and/or proxy PO on requirements.
- Gets each member of the team to give updates at the twice weekly stand up, either in person or through Slack.
- Points raised in the sprint retro will be noted and posted on the Doodle slack retro channel
- Keeps an eye on Jira to ensure tasks are being updated and team members have the correct amount of work in each sprint.
- Closing the previous sprint, starting the current sprint & filling in the sprint goal in Jira.

A Proxy PO within the Doodle group will handle any PO related tasks in the event of the PO being unable to attend a meeting. The proxy PO will then inform the PO of the tasks that were performed in their absence.

A Tech Lead within the Doodle group is responsible for making any technology related decisions during the sprint then informing the whole team of the decisions & the reasons behind those decisions.

#### Sprints

Sprints are 1 week in length, starting on Fridays and finishing on Thursdays.

##### Sprint Goals

| Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 | Sprint 5 | Sprint 6 | Sprint 7 | Sprint 8 | Sprint 9 |
|---|---|---|---|---|---|---|---|---|
|Process | Jira/Planning | POCS/Tech/Arch | Envs | Pipelines | Automation | Refine product | | |

#### Definition of Done

- All code merged to master
- Documentation updated
- Master branch tagged

#### Ceremonies

- Sprint Duration: 1 week
- Planning : Thursdays 8pm
- Standups: Monday / Friday after class
- Demos: Recorded after each sprint and shared
- Retrospectives: Every second Thursday before sprint planning

#### Stand-ups

Stand ups are brief update meetings with a minimum of two held each sprint to ensure everything is on track, three questions are covered.

1. What have you done?
2. What are you going to do?
3. Any impediments?

#### Retrospectives

Retrospectives are held every second sprint to gain feedback and insights into how well things are going.

## Technical

### GitHub

Our repository is on GitHub so to keep things simple and follow best practices we will align with GitHub conventions wherever possible.

[GitHub Style Guide](https://github.com/agis/git-style-guide)

#### Branching strategy

We will adopt a simple branching strategy based on [trunk based development](https://hackernoon.com/trunk-based-development-tbd-for-apps-9b654b6b198c)

[Simple Branching Strategy](https://docs.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops#keep-your-branch-strategy-simple)

#### How to make changes

These are the steps involved in making changes to the repository.

Firstly ensure you have cloned the repository locally, open a command/powershell prompt and follow the steps below

```

mkdir c:\code
cd c:\code
git clone https://github.com/rlennon/Doodle.git
cd .\Doodle

```

You now have the repository cloned locally and are on the **master** branch. Next create a branch and check it out.

```

git checkout -b test-branch

```

You have now created/checked out the test-branch and can make changes in isolation, once you have completed your changes you can then commit them and merge master down to your branch,
this ensures you aren't trying to PR a branch that might have conflicts.

Remember to work in small chunks, commit often.

```

git add *
git commit -m 'A nice descriptive message'
git merge master
git push --set-upstream origin test-branch

```

If there are no conflicts and everything is good then push your branch to origin if you haven't already and open a [Pull Request](https://github.com/rlennon/Doodle/pulls)

### Jira

All work carried out by the team must have a task within Jira, the task should have the correct number of points assigned plus valid Acceptance Criteria.

Tasks should be within sprints, each sprint lasting 1 week. Each team member should only take into the sprint the tasks they can complete during that sprint.

All tasks should be moved to **In Progress** when being worked on & moved to **Done** when the Acceptance Criteria have been met.

### Versioning

Versioning will follow [Semantic guidelines](https://semver.org/)
