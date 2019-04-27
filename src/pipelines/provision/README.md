# Pipelines: provision

This pipeline tests and runs Ansible environments provisioning.

## Requirements

- Git
- Ansible
- Ansible-lint
- ~/hosts-staging.ini/hosts-prod.ini inventories

## steps

The following steps are run:

- Git pull
- Ansible-lint
- Ansible provision to Staging
- Ansible provision to Production

NOTE: the "provision" tag is used during Ansible run to switch the playbook for just provisioning.
