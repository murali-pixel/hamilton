export const example = `from hamilton import dataflow, driver

text_summarization = dataflow.import_module("zilto", "text_summarization")
dr = driver.Driver({}, text_summarization)
# use the driver
`;

export const example2 = `from hamilton import driver
# pip install sf-hamilton-contrib
from hamilton.contrib.user.zilto import text_summarization
dr = driver.Driver({}, text_summarization)
# use the driver`;
