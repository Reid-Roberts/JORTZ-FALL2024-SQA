## same logger from in class worshop to be now implemented in project

import logging


def giveMeLoggingObject():
    format_str = '%(asctime)s:%(message)s'
    file_name  = 'PROJECT-LOGGER.log'
    logging.basicConfig(format=format_str, filename=file_name, level=logging.INFO)
    loggerObj = logging.getLogger('simple-logger')
    return loggerObj
