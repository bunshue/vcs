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
logger = logging.getLogger("mylog")

logger.info("使用logger對象 INFO")
logger.debug("使用logger對象 DEBUG")

logging.debug("使用logging模組 DEBUG")
logging.info("使用logging模組 INFO")
logging.warning("使用logging模組 WARNING")

"""
logger = logging.getLogger("show_patient_IDs")
logger.info(f"reading: {file_name}")
logger.info("finished reading")

logging.debug("程式開始")
for i in range(5):
    logging.debug(f"目前索引 {i}")
logging.debug("程式結束")
"""
print("------------------------------------------------------------")  # 60個
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

print("------------------------------------------------------------")  # 60個
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
print("------------------------------------------------------------")  # 60個


import logging

logging.basicConfig(
    filename="tmp_log_filename06.txt",
    level=logging.INFO,
    format="*** %(levelname)s %(message)s",
)

logger = logging.getLogger("multissl")

HERE = os.path.abspath(os.getcwd())
DEST_DIR = os.path.abspath(os.path.join(HERE, os.pardir, "openssl"))

logger.debug("Call '{}'".format("cccccc"))

url = "dddddd"
logger.info("Downloading OpenSSL from {}".format(url))
src_file = "ffffff"

logger.info("Storing {}".format(src_file))
logger.info("Rebuilding Python modules")
logger.debug("Already has src {}".format(src_file))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import logging

mesg1 = "aaaa"
mesg2 = "bbbb"
function_name = "cccc"
number = 1234

logging.basicConfig(filename="tmp_log_filename07.txt", level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("Sending %r to %r, function : %s", mesg1, mesg2, function_name)
logger.info("sleep(%d)", number)

logger.warning("retrying %s due to %s", function_name, "kkkk")

logger.exception("Error in %s", function_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
import logging

# 獲取logger對象,取名mylog
logger = logging.getLogger("mylog")
# 輸出DEBUG及以上級別的信息，針對所有輸出的第一層過濾
logger.setLevel(level=logging.DEBUG)

# 獲取文件日誌句柄並設置日誌級別，第二層過濾
handler = logging.FileHandler("tmp_log_filename10.txt")
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

with open("tmp_log_filename11.log", "a") as f:
    f.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - 寫了一筆工作紀錄\n')

print("------------------------------------------------------------")  # 60個

# 製作log檔的範例
print("存檔紀念")

f = open("tmp_log_filename12.txt", "w")
f.write("# BUILD INFO\n")
f.write("# Date: %s\n" % time.ctime())
f.close()
"""
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
