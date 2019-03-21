import logging
from time import sleep
from r7insight import R7InsightHandler

# add your token from insightops here
# token = ''
region = 'EU'

log = logging.getLogger('r7insight')
log.setLevel(logging.INFO)
test = R7InsightHandler(token, region)

log.addHandler(test)

log.warn("Warning message")
log.info("Info message")

sleep(10)