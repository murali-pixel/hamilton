# --- START LICENSE (optional)
# --- END LICENSE
# --- START IMPORT SECTION
import logging

logging = logging.getLogger(__name__)
try:
    # non-hamilton imports go here
    pass
except ImportError as e:
    location = __file__[: __file__.rfind("/")]
    logging.error("ImportError: ", e)
    # TODO: make this actionable.
    logging.error(
        "Please install the required packages. Options\n:"
        f" (1): with `pip install -r {location}/requirements.txt`\n"
    )
    # f" (2): with `hamilton dataflow install --module {location}/requirements.txt`")
    raise e

# hamilton imports go here; check for required version if need be.

# --- END IMPORT SECTION

# --- START HAMILTON DATAFLOW


# --- END HAMILTON DATAFLOW
# --- START MAIN CODE
if __name__ == "__main__":
    # Code to create an imaging showing on DAG workflow.
    # run as a script to test Hamilton's execution
    import __init__ as MODULE_NAME

    from hamilton import base, driver

    dr = driver.Driver(
        {},  # CONFIG: fill as appropriate
        MODULE_NAME,
        adapter=base.DefaultAdapter(),
    )
    # saves to current working directory creating dag.png.
    dr.display_all_functions("dag", {"format": "png", "view": False})
# --- END MAIN CODE
