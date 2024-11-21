# __init__.py
# Import necessary modules or packages
import logging

# Define package-level variables
__version__ = "0.1.0"
__author__ = "Kunal Chandra"

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