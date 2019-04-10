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
