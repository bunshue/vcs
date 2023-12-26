# ch15_26.py
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(message)s')
logging.debug('logging message, DEBUG')
logging.info('logging message, INFO')
logging.warning('logging message, WARNING')
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')


