import os
import sys
import time
import logging

"""
如果沒有寫 logging.basicConfig(filename), 則訊息顯示在console畫面
    
記錄等級:
level=logging.WARNING
level=logging.CRITICAL
level=logging.DEBUG
level=logging.INFO
level=logging.ERROR
"""

print("------------------------------------------------------------")  # 60個

print("寫入一些日誌, 存成一個附加的log檔")

logging.basicConfig(
    filename="tmp_log_filename01.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.debug("這是一個日誌訊息 DEBUG")
logging.info("這是一個日誌訊息 INFO")
logging.warning("這是一個日誌訊息 WARNING")
logging.error("這是一個日誌訊息 ERROR")
logging.critical("這是一個日誌訊息 CRITCAL")

# 獲取logger對象,取名 mylog/程式名
# logger = logging.getLogger(__name__)
logger = logging.getLogger("mylog1")

logger.info("使用logger對象 INFO")
logger.debug("使用logger對象 DEBUG")

logging.debug("使用logging模組 DEBUG")
logging.info("使用logging模組 INFO")
logging.warning("使用logging模組 WARNING")

"""
logger = logging.getLogger("mylog1b")
logger.info(f"reading: {file_name}")
logger.info("finished reading")
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import logging

logging.basicConfig(
    filename="tmp_log_filename06.txt",
    level=logging.INFO,  # 只記錄INFO以上等級
    # level=logging.DEBUG,#只記錄DEBUG以上等級
    format="*** %(levelname)s %(message)s",
)

logger = logging.getLogger("mylog2")

logger.debug("這是一個日誌訊息 DEBUG")
logger.info("這是一個日誌訊息 INFO")
logger.warning("這是一個日誌訊息 WARNING")
logger.error("這是一個日誌訊息 ERROR")
logger.critical("這是一個日誌訊息 CRITCAL")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import logging

logging.basicConfig(filename="tmp_log_filename07.txt", level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("AAAAA")
logger.info("BBBBB")
logger.warning("WWWWWW")
logger.exception("EEEEE")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import logging

# 獲取logger對象,取名mylog
logger = logging.getLogger("mylog3")

# 輸出DEBUG及以上級別的信息，針對所有輸出的第一層過濾
logger.setLevel(level=logging.DEBUG)

# 獲取文件日誌句柄並設置日誌級別，第二層過濾
handler = logging.FileHandler("tmp_log_filename10.txt")
handler.setLevel(logging.INFO)

# 生成並設置文件日誌格式，其中name爲上面設置的mylog
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# 獲取流句柄並設置日誌級別，第二層過濾
console = logging.StreamHandler()
console.setLevel(logging.WARNING)

# 爲logger對象添加句柄
logger.addHandler(handler)
logger.addHandler(console)

# 記錄日誌
logger.info("show info")
logger.debug("show debug")
logger.warning("show warning")
logger.debug("這是一個日誌訊息 DEBUG")
logger.info("這是一個日誌訊息 INFO")
logger.warning("這是一個日誌訊息 WARNING")
logger.error("這是一個日誌訊息 ERROR")
logger.critical("這是一個日誌訊息 CRITCAL")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

logging.disable(logging.CRITICAL)  # 停用所有logging

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import logging

"""
msg = u'严重错误！当前运行环境下有中文路径，abu将无法正常运行！请不要使用中文路径名称, 当前环境为{}'.format(
    to_unicode(str(__file__)))
"""
msg = "aaaaaaaaaa"
logging.info(msg)

msg = "error！non English characters in the current running environment,abu will not work properly!"
logging.info(msg)

logging.info("enable example env will only read RomDataBu/csv")

logging.info("disable example env")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
    if not os.path.exists(g_project_log_dir):
        # 创建log文件夹
        os.makedirs(g_project_log_dir)

    # 输出格式规范
    # file_handler = logging.FileHandler(g_project_log_info, 'a', 'utf-8')
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=g_project_log_info,
                        filemode='a'
                        # handlers=[file_handler]
                        )
"""


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
import logging

logger = logging.getLogger("RefactoringTool")

logger=self.logger)

logger.info(msg)

msg = msg % args
logger.debug(msg)


log_debug("Source: %s", line.rstrip("\n"))
log_error("Can't parse docstring in %s line %s: %s: %s",
                           filename, lineno, err.__class__.__name__, err)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# Set up logging handler
level = logging.DEBUG if options.verbose else logging.INFO
logging.basicConfig(format='%(name)s: %(message)s', level=level)
logger = logging.getLogger('lib2to3.main')
logger.info('Output in %r will mirror the input directory %r layout.',
            options.output_dir, input_base_dir)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

logging.info("Start to load dataset")
logging.info("Done with load dataset")
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# logging_tutorial.py

import logging

"""
ref. https://docs.python.org/3/library/logging.html
Level , DEBUG < INFO < WARNING < ERROR < CRITICAL
"""


def ex1():
    # logging.basicConfig(level=logging.DEBUG)
    # will print 'warning message' , 'error message', because the default level is WARNING
    logging.warning("warning message")
    logging.error("error message")
    logging.debug("I told you so - debug")
    logging.info("I told you so - info")


def ex2():
    logging.error("test")
    log1 = logging.getLogger("ma_app")
    log2 = logging.getLogger()
    log1.warning("I told you")
    log2.warning("warning message")


def ex3():
    # will print all message , because the level is DEBUG
    format_log = "%(asctime)s %(levelname)s:%(message)s"
    logging.basicConfig(filename="example.log", format=format_log, level=logging.DEBUG)
    # logging.basicConfig(format=format_log, level=logging.DEBUG)
    logging.debug("This message should go to the log file")
    logging.info("So should this")
    logging.warning("And this, too")


def ex4():
    # multiple-handlers-and-formatter
    logger = logging.getLogger("my_app")
    logger.setLevel(logging.DEBUG)

    log_file = "tmp_my_test_logger.log"
    f_log = logging.FileHandler(log_file, mode="w")
    f_log.setLevel(logging.ERROR)

    c_log = logging.StreamHandler()
    c_log.setLevel(logging.DEBUG)

    format_log = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    f_log.setFormatter(format_log)
    c_log.setFormatter(format_log)

    logger.addHandler(f_log)
    logger.addHandler(c_log)

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")


if __name__ == "__main__":
    # ex1()
    # ex2()
    # ex3()
    ex4()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 設定工作日誌檔名及訊息欄位
logging.basicConfig(
    filename="record.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)


# 設定工作日誌檔名及訊息欄位
logging.basicConfig(
    filename="record.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)


# 設定工作日誌檔名及訊息欄位
logging.basicConfig(
    filename="record.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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
        formater = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )  # 设置输出格式
        self.logger = logging.getLogger("log")  # 定义一个日志收集器
        self.logger.setLevel(logging.INFO)  # 设定级别
        self.fileLogger = handlers.RotatingFileHandler(
            "./test.log", maxBytes=5242880, backupCount=3, encoding="utf-8"
        )  # 输出渠道一 - 文件形式
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

if __name__ == "__main__":
    logger.debug("调试消息")
    logger.info("普通消息")
    logger.warn("警告消息")
    logger.error("错误消息")
    logger.critical("严重错误消息")
    try:
        1 / 0
    except Exception as e:
        logger.excepiton(e)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.WARNING)

logging.warning(HTTP_ERROR_MSG.format(res=exc.response))
logging.warning(HTTP_ERROR_MSG.format(res=exc.response))
logging.error("Connection error")
logging.debug("{}{} ing......".format(self.ptt_head, article.url))
logging.warning(HTTP_ERROR_MSG.format(res=exc.response))
logging.debug("crawler_info......{}".format(res.url))

logging.warning(e)

logging.debug("本文已被刪除")
