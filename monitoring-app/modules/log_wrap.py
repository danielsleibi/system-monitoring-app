import logging
log_file = "./monitoring-app/logfile.log"
log_level = logging.DEBUG
logging.basicConfig(level=log_level, filename=log_file, filemode="w+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger("monitor_app_logger")


def wrap(pre, post):
    """ Wrapper """
    def decorate(func):
        """ Decorator """
        def call(*args, **kwargs):
            """ Actual wrapping """
            pre(func, *args)
            result = func(*args, **kwargs)
            post(func)
            return result
        return call
    return decorate


def entering_get_usage(func, *args):
    """ Pre function logging """
    logger.debug("Entered %s", func.__name__)
    logger.info("Usage type is %s", *args[0])
    if len(args) > 1 and args[1]:
        logger.info("Argument hour is %s", args[1])
        if not args[1] in range(1, 25):
            logger.warn("Argument hour is not in range")


def entering(func, *args):
    """ Pre function logging """
    logger.debug("Entered %s", func.__name__)


def exiting(func):
    """ Post function logging """
    logger.debug("Exited  %s", func.__name__)
