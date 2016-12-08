import logging


def setup_custom_logger(name):
    """
    %(pathname)s Full pathname of the source file where the logging call was issued(if available).
    %(filename)s Filename portion of pathname.
    %(module)s Module (name portion of filename).
    %(funcName)s Name of function containing the logging call.
    %(lineno)d Source line number where the logging call was issued (if available).

    :param name: class name, usually be "__name__"
    :return:
    """
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
