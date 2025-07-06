import logging


logging.basicConfig(filename='app.log',
                    filemode='a',
                    format='%(asctime)s [%(process)d] %(filename)s %(funcName)s>> %(name)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.DEBUG)  # Set the logging level to DEBUG

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')