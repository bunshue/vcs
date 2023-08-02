import logging

mesg1 = 'aaaa'
mesg2 = 'bbbb'
function_name = 'cccc'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Sending %r to %r", mesg1, mesg2)
logger.info("%s run successfully", function_name)
logger.exception("Error in %s", function_name)

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

logger.info("started execution of %s", function_name)

logger.info("running operation...")

logger.info("started execution of %s", function_name)
logger.info("running operation 1")

logger.info("running %s", function_name)
logger.info("processing account %s", function_name)

logger.info("started execution of %s", function_name)

logger.info("sleep(%d)", 1234)

logger.warning("retrying %s due to %s", function_name, 'kkkk')









