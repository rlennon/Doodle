# Process

This page will outline the various processes that we have refined as the project progressed, focusing on both the technical and non-technical sides.

## Non-Tech

### Scrum

//TODO: Some info on our version of SCRUM

#### Team Breakdown

Being a forward thinking company, we like to keep our people both happy and challenged, this means we change roles **A LOT!**

| Role | Week 0 1/3 | Week 1 8/3 | Week 2 15/3 | Week 3 22/3 | Week 4 29/3 | Week 5 5/4 | Week 6 12/4 | Week 7 19/4 |
|---|---|---|---|---|---|---|---|---|
| Scrum Master | Francis | Colin | Conor  | Emmet   | Fiona | Lee | Peter   | Wes |
| Proxy PO     | Conor   | Emmet | Fiona  | Lee     | Peter | Wes | Francis | Colin |
| Tech Lead    | Emmet   | Fiona | Lee    | Peter   | Wes   | Francis | Colin | Conor |

#### Sprints

Sprints are 1 week in length, starting on Fridays and finishing on Thursdays.

General progression of sprints:

- Process / Documentation
- Jira setup / planning / estimation
- POCs and refine technology choices / architecture
- Environments with VMs
- Jenkins and pipelines manually
- Automate Infrastructure as code
- Refine the product / Add checks and balances to the pipelines

#### Definition of Done

- All code merged to master
- Documentation updated
- Master branch tagged

#### Ceremonies

- Sprint Duration: 1 week
- Planning : Thursdays 8pm
- Standups: Monday / Friday after class
- Demos: Recorded after each sprint and shared
- Retrospectives: Thursdays before planning

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

### Versioning

Versioning will follow [Semantic guidelines](https://semver.org/)

## Consideration

- Frameworks
- Database
- Database persistance technology 
- Define the buisness Requirements
- Named queries and database triggers for security 
- Regex for cleansing and validation of data before sending to the database.
