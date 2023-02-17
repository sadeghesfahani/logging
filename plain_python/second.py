from logger import Logger,LoggerSingleton


# logger = Logger('log.log')
#
#
# logger.logFast('Hello, world!')

logger = LoggerSingleton('log.log')


logger.log('second')