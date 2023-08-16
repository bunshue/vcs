import logging

logger = logging.getLogger("untar")

logger.info("finished reading")
logger.debug("Unzipping...")

logging.debug("Untar complete!")
logging.info("Interrupt detected, quiting")
logging.warning("Unknown Error, exiting")






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




