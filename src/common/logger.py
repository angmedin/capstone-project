import logging
import logging.config
from typing import Optional

from utils.singleton_metaclass import SingletonMeta


class Logger(metaclass=SingletonMeta):

    DEFAULT_LOGGER = 'app'

    LOG_CONFIG = {
        "version": 1,
        "root": {
            "handlers": ["console"],
            "level": "DEBUG"
        },
        "handlers": {
            "console": {
                "formatter": "simple",
                "class": "logging.StreamHandler",
                "level": "DEBUG"
            }
        },
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(levelname)s - %(module)s:%(lineno)d [%(threadName)s] : %(message)s",
                "datefmt": "%d-%m-%Y %I:%M:%S"
            }
        }
    }

    @staticmethod
    def setup(config: Optional[dict] = LOG_CONFIG) -> None:
        logging.config.dictConfig(config=config)
