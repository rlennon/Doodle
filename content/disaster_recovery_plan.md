# Doodle Disaster Recovery plan

This document outlines the Doodle DR plan. It follows IBM best practice:

https://www.ibm.com/support/knowledgecenter/en/ssw_ibm_i_73/rzarm/rzarmdisastr.htm

## Goals

The goals of this plan are:

- To minimize interruptions to normal operations
- To limit the extent of disruption and damage
- To minimize the economic impact of the interruption
- To establish alternative means of operation in advance
- To train personnel with emergency procedures
- To provide for smooth and rapid restoration of service

## Personnell

| Role | Name | Contact |
|---|---|---|
| Data Controller | Colin | 7657 |
| Infrastructure Manager | Peter | 5543 |


## Critical Assets

The following are critical assets:

- Doodle Application
- Doodle Application Data (mondoDB)
- Doodle Application infrastructure (VMs)


## Data Backup procedures

All data assets are backed up regularly by the backup server. It is the responsibility of the data controller to monitor the health of this system and respond to any failures

Data backups are stored in the following locations:

- Hot remote online (cloud)
- Cold Local offline (Tape)
- Cold remote offline (Tape safe)

It is necessary to follow this plan for weekly tape cycle/test

- take tapes from tape machine
- select 2 tapes for testing
- run test script
- remove tapes to offline remote storage location

## Disaster Recovery procedures

The purpose of these procedures are to:

- quickly assemble a DR team
- investigate the source and scope of the disaster
- communicate to management
- recover service to DR infrastructure
- restore main infrastructure and restore data
- log incident

In the event of disaster, please do the following:

Call DR hotline (24/7) on 6676 to assemble DR team. team will then assemble and follow the DR checklist:


https://www.ibm.com/support/knowledgecenter/en/ssw_ibm_i_73/rzarm/rzarmdisaactionchecklist.htm

## Recovery steps to Hot site

Here are the steps to follow to recover to our Hot site. the Hot site resides on the Crowsoft esxi host.
There is deployed a exact copy of Doodle infrastructure and replicated data. To switch to hot site:

- confirm data is up-to-date at hot site
- if not, recover from hot backup
- log in and update external Loadbalancer to send traffic to Hot site
- if the LB is down, update DNS records for Hot site


## Restoring the entire system

This outlines the steps to restore the entire Doodle application infrastructure

Firstly, identify new cloud hosts.

- Run the terraform infra code to deploy new VMs
- Run the ansible provision to configure and deploy Doodle application
- Recover data from backup (hot or cold, as available)
- Update Loadbalancer or DNS records

## Disaster plan testing

It is necessary to test this plan by holding regular disaster procedure training. These should be held twice yearly.
The outline for these sessions are:

- review DR documentation and flag and required corrections/updates
- simulate a disaster and recovery
- Log outcomes and improvements

here is checklist :

https://www.ibm.com/support/knowledgecenter/en/ssw_ibm_i_73/rzarm/rzarmtestdisarecplan.htm
