# Ansible configuration management

This code configures VMs and deploys Doodle application.

## Dependencies

- Ansible

## Setup

- edit ```hosts.ini``` with VM IP/hostnames
- review group_vars

## provision

run:

```ansible-playbook -i hosts.ini site.yml```

NOTE: you may need to supply VM credentials and suppress host key checking as follows:

```ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook --ask-pass --ask-sudo-pass -i hosts.ini site.yml```
