# pip install sf-hamilton-contrib
# WARNING: ensure you know what code you're importing!
from hamilton.contrib.user.zilto import text_summarization

from hamilton import driver

dr = driver.Driver({}, text_summarization)
# use the driver
