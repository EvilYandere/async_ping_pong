import logging


class MessageOnlyFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        return record.getMessage()


def get_logger(service_name: str) -> logging.Logger:
    logger: logging.Logger = logging.getLogger(f"{service_name}_logger")
    logger.setLevel(logging.INFO)
    file_handler: logging.FileHandler = logging.FileHandler(f"/app/log/{service_name}.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(MessageOnlyFormatter())
    logger.addHandler(file_handler)
    return logger
