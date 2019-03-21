# Infrastructure POC

This Proof of Concept demonstrates three technologies to provision and configure infrastructure VMs. it uses:
- Vagrant/Virtualbox: for local dev environment provisioning
- Terraform: for production provisioning
- Ansible: for configuration management

## Vagrant

dependencies:

- virtualbox
- ansible
- vagrant
- vagrant-hostmanager plugin

To create:

```
vagrant up
```

## Terraform

Dependencies:

- terraform

Configuration:

Edit file "terraform.tfvars" with your vsphere server credentials

To create:

```
terraform init
terraform plan
terraform apply
```
