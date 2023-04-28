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



