import logging

logging.basicConfig(filename="app.log", level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("Application started")
logger.warning("Memory usage is high")
logger.error("Unable to connect to database")
