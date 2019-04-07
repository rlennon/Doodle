## Prerequisites
To use Jenkins Pipeline, you will need:

Jenkins 2.x or later (older versions back to 1.642.3 may work but are not recommended)

Pipeline plugin, [2] which is installed as part of the "suggested plugins" (specified when running through the Post-installation setup wizard after installing Jenkins).

Read more about how to install and manage plugins in Managing Plugins.

## Defining a Pipeline
Both Declarative and Scripted Pipeline are DSLs [1] to describe portions of your software delivery pipeline. Scripted Pipeline is written in a limited form of Groovy syntax.

Relevant components of Groovy syntax will be introduced as required throughout this documentation, so while an understanding of Groovy is helpful, it is not required to work with Pipeline.

A Pipeline can be created in one of the following ways:

- Through Blue Ocean
After setting up a Pipeline project in Blue Ocean, the Blue Ocean UI helps you write your Pipeline’s Jenkinsfile and commit it to source control.

- Through the classic UI
You can enter a basic Pipeline directly in Jenkins through the classic UI.

- In SCM 
You can write a Jenkinsfile manually, which you can commit to your project’s source control repository. [3]

The syntax for defining a Pipeline with either approach is the same, but while Jenkins supports entering Pipeline directly into the classic UI, it is generally considered best practice to define the Pipeline in a Jenkinsfile which Jenkins will then load directly from source control.

## Through Blue Ocean
If you are new to Jenkins Pipeline, the Blue Ocean UI helps you set up your Pipeline project, and automatically creates and writes your Pipeline (i.e. the Jenkinsfile) for you through the graphical Pipeline editor.

As part of setting up your Pipeline project in Blue Ocean, Jenkins configures a secure and appropriately authenticated connection to your project’s source control repository. Therefore, any changes you make to the Jenkinsfile via Blue Ocean’s Pipeline editor are automatically saved and committed to source control.

Read more about Blue Ocean in the Blue Ocean chapter and Getting started with Blue Ocean page.

## Through the classic UI
A Jenkinsfile created using the classic UI is stored by Jenkins itself (within the Jenkins home directory).

To create a basic Pipeline through the Jenkins classic UI:

If required, ensure you are logged in to Jenkins.

From the Jenkins home page (i.e. the Dashboard of the Jenkins classic UI), click New Item at the top left.

Classic UI left column

In the Enter an item name field, specify the name for your new Pipeline project.
Caution: Jenkins uses this item name to create directories on disk. It is recommended to avoid using spaces in item names, since doing so may uncover bugs in scripts that do not properly handle spaces in directory paths.

Scroll down and click Pipeline, then click OK at the end of the page to open the Pipeline configuration page (whose General tab is selected).

Enter a name, click <strong>Pipeline</strong> and then click <strong>OK</strong>

Click the Pipeline tab at the top of the page to scroll down to the Pipeline section.
Note: If instead you are defining your Jenkinsfile in source control, follow the instructions in In SCM below.

In the Pipeline section, ensure that the Definition field indicates the Pipeline script option.

Enter your Pipeline code into the Script text area.
For instance, copy the following Declarative example Pipeline code (below the Jenkinsfile ( …​ ) heading) or its Scripted version equivalent and paste this into the Script text area. (The Declarative example below is used throughout the remainder of this procedure.)

Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world!' 
            }
        }
    }
}
Toggle Scripted Pipeline (Advanced)
agent instructs Jenkins to allocate an executor (on any available agent/node in the Jenkins environment) and workspace for the entire Pipeline.
echo writes simple string in the console output.
node effectively does the same as agent (above).
Example Pipeline in the classic UI

Note: You can also select from canned Scripted Pipeline examples from the try sample Pipeline option at the top right of the Script text area. Be aware that there are no canned Declarative Pipeline examples available from this field.

Click Save to open the Pipeline project/item view page.

On this page, click Build Now on the left to run the Pipeline.

Classic UI left column on an item

Under Build History on the left, click #1 to access the details for this particular Pipeline run.

Click Console Output to see the full output from the Pipeline run. The following output shows a successful run of your Pipeline.

<strong>Console Output</strong> for the Pipeline

Notes:

You can also access the console output directly from the Dashboard by clicking the colored globe to the left of the build number (e.g. #1).

Defining a Pipeline through the classic UI is convenient for testing Pipeline code snippets, or for handling simple Pipelines or Pipelines that do not require source code to be checked out/cloned from a repository. As mentioned above, unlike Jenkinsfiles you define through Blue Ocean (above) or in source control (below), Jenkinsfiles entered into the Script text area area of Pipeline projects are stored by Jenkins itself, within the Jenkins home directory. Therefore, for greater control and flexibility over your Pipeline, particularly for projects in source control that are likely to gain complexity, it is recommended that you use Blue Ocean or source control to define your Jenkinsfile.

## In SCM
Complex Pipelines are difficult to write and maintain within the classic UI’s Script text area of the Pipeline configuration page.

To make this easier, your Pipeline’s Jenkinsfile can be written in a text editor or integrated development environment (IDE) and committed to source control [3] (optionally with the application code that Jenkins will build). Jenkins can then check out your Jenkinsfile from source control as part of your Pipeline project’s build process and then proceed to execute your Pipeline.

To configure your Pipeline project to use a Jenkinsfile from source control:

Follow the procedure above for defining your Pipeline through the classic UI until you reach step 5 (accessing the Pipeline section on the Pipeline configuration page).

From the Definition field, choose the Pipeline script from SCM option.

From the SCM field, choose the type of source control system of the repository containing your Jenkinsfile.

Complete the fields specific to your repository’s source control system.
Tip: If you are uncertain of what value to specify for a given field, click its ? icon to the right for more information.

In the Script Path field, specify the location (and name) of your Jenkinsfile. This location is the one that Jenkins checks out/clones the repository containing your Jenkinsfile, which should match that of the repository’s file structure. The default value of this field assumes that your Jenkinsfile is named "Jenkinsfile" and is located at the root of the repository.

When you update the designated repository, a new build is triggered, as long as the Pipeline is configured with an SCM polling trigger.

Since Pipeline code (i.e. Scripted Pipeline in particular) is written in Groovy-like syntax, if your IDE is not correctly syntax highlighting your Jenkinsfile, try inserting the line #!/usr/bin/env groovy at the top of the Jenkinsfile, [4] [5] which may rectify the issue.

Built-in Documentation
Pipeline ships with built-in documentation features to make it easier to create Pipelines of varying complexities. This built-in documentation is automatically generated and updated based on the plugins installed in the Jenkins instance.

The built-in documentation can be found globally at: localhost:8080/pipeline-syntax/, assuming you have a Jenkins instance running on localhost port 8080. The same documentation is also linked as Pipeline Syntax in the side-bar for any configured Pipeline project.

Classic UI left column on an item

## Snippet Generator
The built-in "Snippet Generator" utility is helpful for creating bits of code for individual steps, discovering new steps provided by plugins, or experimenting with different parameters for a particular step.

The Snippet Generator is dynamically populated with a list of the steps available to the Jenkins instance. The number of steps available is dependent on the plugins installed which explicitly expose steps for use in Pipeline.

To generate a step snippet with the Snippet Generator:

Navigate to the Pipeline Syntax link (referenced above) from a configured Pipeline, or at localhost:8080/pipeline-syntax.

Select the desired step in the Sample Step dropdown menu

Use the dynamically populated area below the Sample Step dropdown to configure the selected step.

Click Generate Pipeline Script to create a snippet of Pipeline which can be copied and pasted into a Pipeline.