from hamilton import dataflow, driver

# download and load the module -- WARNING: ensure you know what code you're importing!
text_summarization = dataflow.import_module("text_summarization", "zilto")
dr = driver.Driver({}, text_summarization)
# use the driver
