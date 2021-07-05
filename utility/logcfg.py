"""Logger for Car Management"""
import logging
import logging.config
import logging.handlers


def setup_logger(filename, console_level, file_level, console_output=True) -> logging.Logger:
    """
    Method to setup the logger for application
    Args:
        filename: Name of the file where to store log
        console_level: Console log level
        file_level: File log level
        console_output: It is the boolean flag whether we want log on console or not.
                        By default it is set to true.
    """
    root_logger = logging.getLogger()
    if not len(root_logger.handlers):
        if console_output:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(
                logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S'))
            console_handler.setLevel(console_level)
            root_logger.addHandler(console_handler)
        file_handler = logging.handlers.RotatingFileHandler(
            filename)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(name)s %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S'))
        file_handler.setLevel(file_level)
        root_logger.setLevel(file_level)
        root_logger.addHandler(file_handler)
    return root_logger
