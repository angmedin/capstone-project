from common.logger import Logger

def start() -> None:
    logger = Logger()
    logger.log_info("My message")

if __name__ == '__main__':
    start()