import logging

LOGGING_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

logging.basicConfig(format=LOGGING_FORMAT)
logging.getLogger().setLevel(logging.INFO)
