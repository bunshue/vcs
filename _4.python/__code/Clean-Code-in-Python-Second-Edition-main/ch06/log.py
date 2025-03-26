import logging
from logging import handlers


class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        # formater = logging.Formatter('%(message)s')  # 只要原本信息
        formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')  # 设置输出格式
        self.logger = logging.getLogger('log')  # 定义一个日志收集器
        self.logger.setLevel(logging.INFO)  # 设定级别
        self.fileLogger = handlers.RotatingFileHandler("./test.log", maxBytes=5242880, backupCount=3,
                                                       encoding='utf-8')  # 输出渠道一 - 文件形式
        self.console = logging.StreamHandler()  # 输出渠道二 - 控制台
        self.console.setLevel(logging.INFO)  # 控制台输出级别
        self.console.setFormatter(formater)  # 输出渠道对接输出格式
        self.fileLogger.setFormatter(formater)
        self.logger.addHandler(self.fileLogger)  # 日志收集器对接输出渠道
        self.logger.addHandler(self.console)

    def debug(self, msg):
        self.logger.debug(msg=msg)

    def info(self, msg):
        self.logger.info(msg=msg)

    def warn(self, msg):
        self.logger.warning(msg=msg)

    def error(self, msg):
        self.logger.error(msg=msg)

    def critical(self, msg):
        self.logger.critical(msg=msg)

    def excepiton(self, msg):
        self.logger.exception(msg=msg)


logger = Logger()

if __name__ == '__main__':
    logger.debug('调试消息')
    logger.info('普通消息')
    logger.warn('警告消息')
    logger.error('错误消息')
    logger.critical('严重错误消息')
    try:
        1 / 0
    except Exception as e:
        logger.excepiton(e)
