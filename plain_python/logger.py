import time


class Logger:
    loggerInstance = None

    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as f:
            print('Logging...')
            time.sleep(10)
            print(message)
            f.write(message)

    def logFast(self, message):
        with open(self.filename, 'a') as f:
            f.write(message)


class LoggerSingleton:
    loggerInstance = None

    def __init__(self, filename):
        if not LoggerSingleton.loggerInstance:
            LoggerSingleton.loggerInstance = Logger(filename)
        else:
            LoggerSingleton.loggerInstance.filename = filename

    def __getattr__(self, name):
        return getattr(self.loggerInstance, name)

    def log(self, message):
        self.loggerInstance.log(message)

    def logFast(self, message):
        self.loggerInstance.logFast(message)
