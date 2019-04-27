# Pipelines: Deploy Production env

This pipeline deploys Doodle application to production following successful Artifactory build+staging deploy pipeline runs

## Requirements

- Git
- Ansible
- Ansible-lint
- ~/hosts-prod.ini inventory

## Steps

The following steps are run:

- Git pull
- Ansible-lint
- Ansible deploy run to production env
- service validation test
- service security test

NOTE: the "deploy" tag is used during Ansible run to switch the playbook for just deployment.
