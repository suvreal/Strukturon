from logging import getLogger, DEBUG, basicConfig

LOGGER = getLogger("Strukturon")
LOGGER.setLevel(DEBUG)  # TODO: set level dynamically according to call
basicConfig()