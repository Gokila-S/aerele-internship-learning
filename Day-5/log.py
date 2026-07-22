import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

logger.debug("Debugging application")
logger.info("User logged in")
logger.warning("Low disk space")
logger.error("Database connection failed")
logger.critical("Application crashed")
