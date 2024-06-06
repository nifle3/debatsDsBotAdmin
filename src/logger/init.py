from loguru import logger, Logger
from sys import stdout


def init_log(env : str) -> Logger:
    logger.remove(0)

    env = env.lower()
    match env:
        case "prod":
            logger.add(stdout, format="{time} | {level} | {message}", serialize=True, level="INFO")
        case "debug":
            logger.add(stdout, format="{time} | {level} | {message}", level="DEBUG")
        case _:
            logger.add(stdout, format="{time} | {level} | {message}", level="DEBUG")
            logger.warning(f'environment type {env} is invalid. Apply default DEBUG')

    return logger
