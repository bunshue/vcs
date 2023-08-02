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











