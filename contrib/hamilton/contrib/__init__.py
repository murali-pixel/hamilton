try:
    from .version import VERSION as __version__  # noqa: F401
except ImportError:
    from version import VERSION as __version__  # noqa: F401

from hamilton import telemetry


def track(module_name: str):
    telemetry.create_and_send_contrib_use(module_name, __version__)
