# Pipelines: Deploy staging env

This pipeline deploys Doodle application to staging following successful Artifactory build pipeline

## Requirements

- Git
- Ansible
- Ansible-lint
- ~/hosts-staging.ini inventory

## Steps

The folllowing steps are run:

- Git pull
- Ansible-lint
- Ansible deploy run to staging env
- service validation test
- service security test
- if all pass, run deploy_prod pipeline

NOTE: the "deploy" tag is used during Ansible run to switch the playbook for just deployment.
