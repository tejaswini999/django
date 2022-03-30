from Employee_Project.settings import BASE_DIR
import os
import logging.config


def get_logger():
    """
    creating and configuring custom logger to log data in file
    """
    logging.config.fileConfig(os.path.join(BASE_DIR, 'logging_config.ini'))
    logger = logging.getLogger()
    return logger
