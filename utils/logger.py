import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.ERROR)  # Can be changed based on configuration

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)  # Change to INFO or WARNING in production

    # Modified formatter to include filename and line number details
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    
    # To ensure multiple log handlers are not added to the same logger (avoid duplicate logs)
    if not logger.handlers:
        logger.addHandler(ch)
    
    return logger
