import logging

def get_app_logger(name):
    # Prefix the logger name with "app" for clarity
    logger_name = f"app.{name}"
    
    # If there are redundant parts of the path, you can remove them here
    # For example, if name is 'app.services.validation_service', you can strip out the 'app.'
    # Adjust the replacement as per your needs
    logger_name = logger_name.replace('app.app.', 'app.')
    
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)  # Adjust based on app's need
    logger.propagate = False  # This ensures the log message doesn't propagate to other loggers

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)  # Adjust based on app's need

    formatter = logging.Formatter('%(asctime)s - %(name)s.py:%(lineno)d - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    
    # Check if handlers already exist before adding to prevent duplicates
    if not logger.hasHandlers():
        logger.addHandler(ch)
    
    return logger
