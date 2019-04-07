# Doodle infrastructure

Here is Doodle application infrastructure defined as terraform code.

## Dependencies

The following software is required on your client:

- Terraform

## Configure

Edit file ```terraform.tfvars``` with esxi server credentials

## provision

To provision the application infrastructure, first run:

```
terraform init
```

to initialise terraform and download any plugins/requirements.

Then connect to LYIT VPN and run:

```
terraform plan
terraform apply
```
