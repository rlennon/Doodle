# Vagrant 

This deploys the full doodle application stack on your local workstation using Vagrant 

## Dependencies

- Vagrant
- Virtualbox
- Ansible
- vagrant-hostmanager plugin

## Create

To create the environment, run:


```
vagrant up
```

This will deploy the VMs in virtualbox before handing over to ansible for configuration

## Usage

After deployment completes, the following endpoints are available:

- web.internal.tld:8080
- api.internal.tld:8080

note: these hostnames are dependent on the vagrant-hostmanager plugin. if this is not installed or working, please try the IPs directly:

- 10.0.1.201:8080
- 10.0.1.202:8080
