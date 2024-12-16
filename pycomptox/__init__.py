# __init__.py
# Import necessary modules or packages
import logging

# Initialization code
def initialize_package(config=None):
    """
    Initialize the package with optional configuration.

    Args:
        config (dict, optional): Configuration dictionary for package setup.
    """
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Apply configuration settings if provided
    if config:
        logger.info("Applying configuration...")
        for key, value in config.items():
            logger.info(f"{key} = {value}")

    logger.info("Package initialized successfully!")

initialize_package()