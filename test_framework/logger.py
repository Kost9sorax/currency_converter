import logging


class Logger:
    def __init__(self):
        logger = logging.getLogger("main")
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] [%(process)s] %(message)s',
            '%H:%M:%S'
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.info("Run")
        self.print = logger


log = Logger()