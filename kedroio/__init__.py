import logging

__version__ = "0.1.0"

logging.getLogger("kedro-io").addHandler(logging.NullHandler())
