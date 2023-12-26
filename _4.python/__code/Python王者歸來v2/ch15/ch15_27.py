# ch15_27.py
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s : %(message)s')
logging.debug('logging message.')
logging.info('logging message.')
logging.warning('logging message')
logging.error('logging message')
logging.critical('logging message')


