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









