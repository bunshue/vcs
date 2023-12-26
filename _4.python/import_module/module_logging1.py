
import sys

print('寫入一些日誌')

import logging

logging.basicConfig(filename = 'log_filename.txt', level = logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('這是一個日誌訊息 DEBUG')
logging.info('這是一個日誌訊息 INFO')
logging.warning('這是一個日誌訊息 WARNING')
logging.error('這是一個日誌訊息 ERROR')
logging.critical('這是一個日誌訊息 CRITCAL')

"""
2023-12-25 13:23:29,817 - DEBUG - 這是一個日誌訊息 DEBUG
2023-12-25 13:23:29,819 - INFO - 這是一個日誌訊息 INFO
2023-12-25 13:23:29,819 - WARNING - 這是一個日誌訊息 WARNING
2023-12-25 13:23:29,819 - ERROR - 這是一個日誌訊息 ERROR
2023-12-25 13:23:29,819 - CRITICAL - 這是一個日誌訊息 CRITCAL
"""

print('------------------------------------------------------------')	#60個

import logging
#不知道這樣是把log寫到哪?
logging.basicConfig(level=logging.DEBUG)    # 等級是DEBUG
logging.debug('logging message, DEBUG')
logging.info('logging message, INFO')
logging.warning('logging message, WARNING')
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')

print('------------------------------------------------------------')	#60個

sys.exit()


logger = logging.getLogger("untar")

logger.info("finished reading")
logger.debug("Unzipping...")

logging.debug("Untar complete!")
logging.info("Interrupt detected, quiting")
logging.warning("Unknown Error, exiting")



print('------------------------------------------------------------')	#60個


'''
logger = logging.getLogger("untar")
logger = logging.getLogger("unzip")
logger = logging.getLogger("show_patient_IDs")

logger.info(f'reading: {file_name}')
logger.info("finished reading")
logger.debug("Unzipping...")
logger.debug(f"Unzipping {file_name}")
logger.debug("Untarring...")

logging.debug(f"Found: {file_info.name}")
logging.debug("Untar complete!")
logging.info("Interrupt detected, quiting")
logging.warning("Unknown Error, exiting", exc_info=e)
logging.debug("Unzip complete!")
'''

print('------------------------------------------------------------')	#60個

import logging
import os

print('start here')
logging.basicConfig(level=logging.INFO, format="*** %(levelname)s %(message)s")

log = logging.getLogger("multissl")

HERE = os.path.abspath(os.getcwd())
DEST_DIR = os.path.abspath(os.path.join(HERE, os.pardir, "openssl"))


log.debug("Call '{}'".format('cccccc'))

url = 'dddddd'
log.info("Downloading OpenSSL from {}".format(url))
src_file = 'ffffff'
log.info("Storing {}".format(src_file))
log.info("Rebuilding Python modules")

log.debug("Already has src {}".format(src_file))


print('------------------------------------------------------------')	#60個

import logging

mesg1 = 'aaaa'
mesg2 = 'bbbb'
function_name = 'cccc'
number = 1234
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Sending %r to %r, function : %s", mesg1, mesg2, function_name)
logger.info("sleep(%d)", number)

logger.warning("retrying %s due to %s", function_name, 'kkkk')

logger.exception("Error in %s", function_name)

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)





print('------------------------------------------------------------')	#60個












print('------------------------------------------------------------')	#60個




