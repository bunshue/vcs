import os
import sys
import time

"""
記錄等級:

level=logging.WARNING

level=logging.CRITICAL


"""

print("------------------------------------------------------------")  # 60個

print("寫入一些日誌")

import logging

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

"""
2023-12-25 13:23:29,817 - DEBUG - 這是一個日誌訊息 DEBUG
2023-12-25 13:23:29,819 - INFO - 這是一個日誌訊息 INFO
2023-12-25 13:23:29,819 - WARNING - 這是一個日誌訊息 WARNING
2023-12-25 13:23:29,819 - ERROR - 這是一個日誌訊息 ERROR
2023-12-25 13:23:29,819 - CRITICAL - 這是一個日誌訊息 CRITCAL
"""

print("------------------------------------------------------------")  # 60個

import logging

logging.basicConfig(
    filename="tmp_log_filename02.txt",
    level=logging.DEBUG)

logging.debug("logging message, DEBUG")
logging.info("logging message, INFO")
logging.warning("logging message, WARNING")
logging.error("logging message, ERROR")
logging.critical("logging message, CRITICAL")

print("------------------------------------------------------------")  # 60個

import logging

logging.basicConfig(
    filename="tmp_log_filename06.txt",
    level=logging.DEBUG,
    format="%(asctime)s")


print("------------------------------------------------------------")  # 60個

import logging

logging.basicConfig(
    filename="tmp_log_filename07.txt",
    level=logging.DEBUG,
    format="%(asctime)s : %(message)s")

print("------------------------------------------------------------")  # 60個

logger = logging.getLogger("untar")

logger.info("finished reading")
logger.debug("Unzipping...")
logging.debug("Untar complete!")
logging.info("Interrupt detected, quiting")
logging.warning("Unknown Error, exiting")

print("------------------------------------------------------------")  # 60個

"""
logger = logging.getLogger("untar")
logger = logging.getLogger("unzip")
logger = logging.getLogger("show_patient_IDs")

logger.info(f'reading: {file_name}')
logger.info("finished reading")
logger.debug("Unzipping...")
logger.debug(f"Unzipping {file_name}")
logger.debug("Untarring...")

logging.debug(f"Found: {file_info.name}")
logging.debug("Untar complete!")
logging.info("Interrupt detected, quiting")
logging.warning("Unknown Error, exiting", exc_info=e)
logging.debug("Unzip complete!")
"""

print("------------------------------------------------------------")  # 60個

import logging

print("start here")
logging.basicConfig(
    filename="tmp_log_filename08.txt",
    level=logging.INFO,
    format="*** %(levelname)s %(message)s")

log = logging.getLogger("multissl")

HERE = os.path.abspath(os.getcwd())
DEST_DIR = os.path.abspath(os.path.join(HERE, os.pardir, "openssl"))


log.debug("Call '{}'".format("cccccc"))

url = "dddddd"
log.info("Downloading OpenSSL from {}".format(url))
src_file = "ffffff"
log.info("Storing {}".format(src_file))
log.info("Rebuilding Python modules")

log.debug("Already has src {}".format(src_file))


print("------------------------------------------------------------")  # 60個

import logging

mesg1 = "aaaa"
mesg2 = "bbbb"
function_name = "cccc"
number = 1234

logging.basicConfig(
    filename="tmp_log_filename09.txt",
    level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Sending %r to %r, function : %s", mesg1, mesg2, function_name)
logger.info("sleep(%d)", number)

logger.warning("retrying %s due to %s", function_name, "kkkk")

logger.exception("Error in %s", function_name)

logging.basicConfig(
    filename="tmp_log_filename10.txt",
    level=logging.INFO,
    format="%(levelname)s: %(message)s")

logger = logging.getLogger(__name__)

logging.basicConfig(
    filename="tmp_log_filename11.txt",
    level=logging.INFO,
    format="%(message)s")

logger = logging.getLogger(__name__)

print("------------------------------------------------------------")  # 60個

import logging

logging.basicConfig(
    filename="tmp_log_filename12.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s : %(message)s"
)

logging.debug("logging message.")
logging.info("logging message.")
logging.warning("logging message")
logging.error("logging message")
logging.critical("logging message")

print("------------------------------------------------------------")  # 60個

import logging

logging.debug("程式開始")
for i in range(5):
    logging.debug(f"目前索引 {i}")
logging.debug("程式結束")

print("------------------------------------------------------------")  # 60個

import logging

logging.debug("程式開始")


def factorial(n):
    logging.debug(f"factorial {n} 計算開始")
    ans = 1
    for i in range(n + 1):
        ans *= i
        logging.debug("i = " + str(i) + ", ans = " + str(ans))
    logging.debug(f"factorial {n} 計算結束")
    return ans


num = 5
print(f"factorial({num}) = {factorial(num)}")
logging.debug("程式結束")


import logging

logging.debug("程式開始")


def factorial(n):
    logging.debug(f"factorial {n} 計算開始")
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        logging.debug("i = " + str(i) + ", ans = " + str(ans))
    logging.debug(f"factorial {n} 計算結束")
    return ans


num = 5
print(f"factorial({num}) = {factorial(num)}")
logging.debug("程式結束")

print("------------------------------------------------------------")  # 60個

import logging

logging.debug("程式開始")


def factorial(n):
    logging.debug(f"factorial {n} 計算開始")
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        logging.debug("i = " + str(i) + ", ans = " + str(ans))
    logging.debug(f"factorial {n} 計算結束")
    return ans


num = 5
print(f"factorial({num}) = {factorial(num)}")
logging.debug("程式結束")

print("------------------------------------------------------------")  # 60個

import logging


logging.debug("程式開始")


def factorial(n):
    logging.debug(f"factorial {n} 計算開始")
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        logging.debug("i = " + str(i) + ", ans = " + str(ans))
    logging.debug(f"factorial {n} 計算結束")
    return ans


num = 5
print(f"factorial({num}) = {factorial(num)}")
logging.debug("程式結束")

print("------------------------------------------------------------")  # 60個

import logging

logging.disable(logging.CRITICAL)  # 停用所有logging

logging.debug("程式開始")


def factorial(n):
    logging.debug("factorial %s 計算開始" % n)
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        logging.debug("i = " + str(i) + ", ans = " + str(ans))
    logging.debug("factorial %s 計算結束" % n)
    return ans


num = 5
print("factorial(%d) = %d" % (num, factorial(num)))
logging.debug("程式結束")


print("------------------------------------------------------------")  # 60個
'''
import logging

# 獲取logger對象,取名mylog
logger = logging.getLogger("mylog")
# 輸出DEBUG及以上級別的信息，針對所有輸出的第一層過濾
logger.setLevel(level=logging.DEBUG)

# 獲取文件日誌句柄並設置日誌級別，第二層過濾
handler = logging.FileHandler("tmp_log_filename20.txt")
handler.setLevel(logging.INFO)	

# 生成並設置文件日誌格式，其中name爲上面設置的mylog
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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

print("------------------------------------------------------------")  # 60個
print("不使用 logging 的 logging")

# 製作 log 檔 每執行一次, 存一筆資料在log檔, 附加模式

with open("tmp_log_filename31.log", "a") as f:
    f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - 寫了一筆工作紀錄\n')

print("------------------------------------------------------------")  # 60個

# 製作log檔的範例
print("存檔紀念")

f = open("tmp_log_filename32.txt", "w")
f.write("# BUILD INFO\n")
f.write("# Date: %s\n" % time.ctime())
f.close()
'''
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


