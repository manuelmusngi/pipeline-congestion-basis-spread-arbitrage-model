import logging
from typing import Optional


def setup_logger(name: str = "pipeline_model",
                 level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(level)
    handler = logging.StreamHandler()
    fmt = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(handler)
    return logger


logger = setup_logger()
