import logging
from typing import Optional
from utils.singleton_metaclass import SingletonMeta


class Logger(metaclass=SingletonMeta):

    default_logger = 'app'

    def __init__(self, logger_name: Optional[str] = None) -> None:
        self.logger = logging.getLogger(logger_name or self.default_logger)
        self.setup()

    def setup(self) -> None:
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.FileHandler('logs/messages.log', mode='w'))

    def log_info(self, msg: object) -> None:
        self.logger.log(level=logging.INFO, msg=msg)
