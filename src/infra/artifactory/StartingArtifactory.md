## Starting up Artifactory

1.	Make sure you are a root user in the server by typing
sudo su

2.	create a folder called jfrog
mkdir jfrog

3.	Go to jfrog download website 
https://jfrog.com/open-source/

4.	scroll down untill you see an Artfifactory download zip and put it into the jfrog directory.  

5.	When I clicked the download zip, at the bootom right of the screen I clicked show more and then I copied the link address and done a 
wget link address 

6.	In jfrog directory, re-name the link you downloaded to jfrog-artifactory-oss-6.9.0.zip

7.	Unzip the jfrog-artifactory-oss-6.9.0.zip 

8.	Cd into unzipped folder and cd into bin

9.	Then type
Nohup sh artifactory.sh &

10.	The type
Tail -f nohup.out

11.	Artifactory should now be installed.Type
hostname -i

To get ip address

12.	Type ip address with :8081 into browser. For example
127.0.1.2:8081

13.	When in Artifactory, do not skip steps. Type in password and skip the rest.
