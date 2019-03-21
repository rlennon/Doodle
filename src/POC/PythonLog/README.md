# python logging POC

This Proof of concept demonstrates python application logging with the "InsightOps" SaaS. 

To use, first create a test account at insightops:

```
https://www.rapid7.com/try/insight/
```

create a new log TOKEN. see here for instructions:

```
https://insightops.help.rapid7.com/docs/python
```

Then add token to python script. 

once run you will see logs in insightops interface

`logtest.py` demonstrates basic info/warn/error logs.
`metrictest.py` demonstrates application metrics

NOTE: you need the following python module dependecies:

```
pip install r7insight_python psutil
```