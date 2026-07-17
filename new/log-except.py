import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("Error while performing division")
