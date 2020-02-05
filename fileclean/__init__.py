from loguru import logger

logger.add("log.log", level="INFO")


class PathNotFoundError(Exception):
    pass
