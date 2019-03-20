import time
import logging
from r7insight import R7InsightHandler, metrics

# add your token from insightops here
# token = ''
region = 'EU'

TEST = metrics.Metric(token, region)


@TEST.metric()
def function_one(t):
    """A dummy function that takes some time."""
    time.sleep(t)



function_one(1)
