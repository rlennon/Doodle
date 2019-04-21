## How to Install JFrog Artifactory on Ubuntu 16.04

The easiest way of installing and running Artifactory on Ubuntu 18.04/16,04 is by using Docker. The process is straightforward without dependency/permission hurdles. You just install Docker, download Artifactory image and spin a container.

## Step 1: Install Docker Engine
Install Docker using our guide: How to install Docker CE on Ubuntu / Debian / Fedora / Arch / CentOS. For a quick start, here is the process.

Install packages to allow apt to use a repository over HTTPS:
        sudo apt -y install apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common

Add Docker’s official GPG key:
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Add stable repository:
        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

Install Docker CE:
        sudo apt update && sudo apt -y install docker-ce

If you would like to use Docker as a non-root user, you should now consider adding your user to the “docker” group with something like:
        sudo usermod -aG docker $USER

Run the command below to see a version of docker installed.
        docker version

## Step 2: Download JFrog Artifactory Docker image

Pull the latest Docker image of JFrog Artifactory.
        docker pull docker.bintray.io/jfrog/artifactory-oss:latest

Confirm Docker images:
        docker images

## Step 3: Create Data Directory

Create data directory on host system to ensure data used on container is persistent.
        sudo mkdir -p /jfrog/artifactory
        sudo chown -R 1030 /jfrog/

## Step 4: Start JFrog Artifactory container

To start an Artifactory container, use the command:
        docker run --name artifactory -d -p 8081:8081 \
         -v /jfrog/artifactory:/var/opt/jfrog/artifactory \
         docker.bintray.io/jfrog/artifactory-oss:latest

You can pass Java system properties to the JVM running Artifactory using EXTRA_JAVA_OPTIONS. Check more on Docker setup link. See example below.
        docker run --name artifactory -d -p 8081:8081 \
         -v /jfrog/artifactory:/var/opt/jfrog/artifactory \
         -e EXTRA_JAVA_OPTIONS='-Xms512m -Xmx2g -Xss256k -XX:+UseG1GC' \
         docker.bintray.io/jfrog/artifactory-pro:latest

## Step 5: Running JFrog Artifactory container with SystemdSystemd is the default init system for Ubuntu 18.04/16.04. We can use it to manage JFrog Artifactory container.

Create Artifactory service unit file.
        sudo vim /etc/systemd/system/artifactory.service
Add:
        [Unit]
        Description=Setup Systemd script for Artifactory Container
        After=network.target

        [Service]
        Restart=always
        ExecStartPre=-/usr/bin/docker kill artifactory
        ExecStartPre=-/usr/bin/docker rm artifactory
        ExecStart=/usr/bin/docker run --name artifactory -p 8081:8081 \
          -v /jfrog/artifactory:/var/opt/jfrog/artifactory \
         docker.bintray.io/jfrog/artifactory-oss:latest
        ExecStop=-/usr/bin/docker kill artifactory
        ExecStop=-/usr/bin/docker rm artifactory

        [Install]
        WantedBy=multi-user.target

Reload systemd.
        sudo systemctl daemon-reload

Then start Artifactory container with systemd.
        sudo systemctl start artifactory

Enable it to start at system boot.
        sudo systemctl enable artifactory

Status can be checked with:
        sudo systemctl status artifactory

## Step 6: Access Artifactory Web Interface

Artifactory can be accessed using the following URL:
        http://172.28.25.122:8081/artifactory

You should see Artifactory welcome page.