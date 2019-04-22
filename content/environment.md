# Environments

Here we describe the various application environments and links to technologies documentation.


# TOC

- [Environments](#environments)
  - [Local Development Environment](#local-development-environment)
    - [Setup](#setup)
    - [FAQ / KB](#faq--kb)
  - [Hosted Environment](#hosted-environment)
    - [Setup](#setup-1)
    - [FAQ / KB](#faq--kb-1)

## Local Development Environment

The local development environment uses Vagrant, Ansible and Virtualbox. When deployed it sets up the full Doodle application stack on your workstation for testing.

### Setup

please see documentation here:
- [Vagrant](../src/infra/vagrant/README.md)

### FAQ / KB

## Hosted Environment

The staging and production environments are hosted in LYIT-DC esxi virtual hosts. Architecture VMs are deployed manually with Terraform "Infrastructure as Code".

Configuration management is carried out by Ansible. A pipeline is setup in Jenkins to test and continuously provision to staging VMs using the Ansible code. Production VMs are provisioned manually.  

### Setup

see documentation here:

- [Terraform](../src/infra/terraform/README.md)
- [Ansible](../src/infra/ansible/README.md)

### FAQ / KB
