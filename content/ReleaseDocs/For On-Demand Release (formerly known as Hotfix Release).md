For On-Demand Release (formerly known as Hotfix Release)

On-Demand release is an unplanned release.  If there's a high priority and/or
big impact bug/issue that must be fixed IMMEDIATELY to support business
continuity then an On-Demand release will be considered ASAP.  This release must
follow the guidance of Change Management.

| **Steps** | **Task**                                                                                    | **Cut Off Date & Time**          | **Deployment Date & Time**    | **Team Member**                          |
|-----------|---------------------------------------------------------------------------------------------|----------------------------------|-------------------------------|------------------------------------------|
| 1         | Create an On-Demand Release Note page                                                       | ASAP after CR release announced  |                               | Release Manager                          |
| 2         | Create a **Normal Change Request**                                                          | ASAP after CR release announced  |                               | Delivery Team (Dev, QE)                  |
| 3         | Update Release Calendar with Normal CR Update On-Demand Release Note page with Normal CR \# |                                  |                               | Release Manager                          |
| 4         | Create QE Stage and Production Sign-Off subtask                                             | ASAP                             |                               | Delivery Team                            |
| 5         | Create Implementation subtask tickets                                                       | ASAP                             |                               | Delivery Team                            |
| 6         | Submit CR for Assessment and Approval                                                       |                                  |                               | Delivery Team                            |
| 7         | Code Deployment to Stage                                                                    |                                  | ASAP, when fixed is available | QE, DevOps                               |
| 8         | QE provides sign-off (close assigned Stage subtask) after Stage Testing                     |                                  |                               | QEs                                      |
| 9         | Update Implementation subtask tickets with Final Build Version                              | Immediately after Stage sign-off |                               | QE                                       |
| 10        | Create Release meeting invite                                                               |                                  |                               | Release Manager                          |
| 11        | Deployment to Production & DR                                                               |                                  | On Demand                     | DevOps                                   |
| 12        | Production Validation                                                                       |                                  |                               | All                                      |
| 13        | QE & PO provide sign-off (close assigned Production subtask)                                | After PROD deployment            |                               | QE PO will provide sign-off if available |
| 14        | Close ticket/ subtask                                                                       | After PROD deployment            |                               | DevOps                                   |

-   Attach Test Plan to CR (if any)
