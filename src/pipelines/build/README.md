# Pipelines: Build

This pipeline builds the application package and sends to Artifactory repository.

## Requirements

- Git
- Python+Pip
- Nosetests
- Pylint
- Artifactory service
- sonarqube service


## Steps

- Git Pull
- Package prep
- Code coverage Testing
- Sonarqube static code analysis
- package tar
- artifactory load
- if all pass: run deploy pipelines
