from logger import Logger, LoggerSingleton

# logger = Logger('log.log')
#
#
# logger.log('Hello, world!')


logger = LoggerSingleton('log.log')

logger.log('Hello, world!')
