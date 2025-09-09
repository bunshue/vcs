"""

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 取得 CPU 個數 3個方法

import psutil

"""有psutil，使用psutil.cpu_count计算cpu个数"""
g_cpu_cnt = psutil.cpu_count(logical=True) * 1
print("g_cpu_cnt =", g_cpu_cnt)

import os

g_cpu_cnt = os.cpu_count()
print("g_cpu_cnt =", g_cpu_cnt)

import multiprocessing as mp

g_cpu_cnt = mp.cpu_count()
print("g_cpu_cnt =", g_cpu_cnt)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


import os
import re
import platform
import sys
import warnings
from enum import Enum
from os import path

import numpy as np
import pandas as pd


# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊ 数据目录 start ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
"""
    abu 文件目录根目录
    windows应该使用磁盘空间比较充足的盘符，比如：d://, e:/, f:///

    eg:
    root_drive = 'd://'
    root_drive = 'e://'
    root_drive = 'f://'
"""
print("ddddddddd")

root_drive = path.expanduser("~")

print("root_drive =", root_drive)

print("__file__ :", __file__)
print("__file__ :", __file__)
print("aaa")
new_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(str(__file__))), os.path.pardir)
)
# 改变路径
root_drive = new_path
print("root_drive is change to {}".format(root_drive))

"""abu数据缓存主目录文件夹"""
g_project_root = path.join(root_drive, "abu")
"""abu数据文件夹 ~/abu/data"""
g_project_data_dir = path.join(g_project_root, "data")
"""abu日志文件夹 ~/abu/log"""
g_project_log_dir = path.join(g_project_root, "log")
"""abu数据库文件夹 ~/abu/db"""
g_project_db_dir = path.join(g_project_root, "db")
"""abu缓存文件夹 ~/abu/cache"""
g_project_cache_dir = path.join(g_project_data_dir, "cache")
"""abu项目数据主文件目录，即项目中的RomDataBu位置"""
g_project_rom_data_dir = path.join(
    path.dirname(path.abspath(path.realpath(__file__))), "../RomDataBu"
)

"""abu日志文件 ~/abu/log/info.log"""
g_project_log_info = path.join(g_project_log_dir, "info.log")

"""hdf5做为金融时间序列存储的路径"""
g_project_kl_df_data = path.join(g_project_data_dir, "df_kl.h5")

_p_dir = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir)
)

# 不再使用hdf5做为默认，有windows用户的hdf5环境有问题
"""使用书中相同的沙盒数据环境，RomDataBu/csv内置的金融时间序列文件"""
g_project_kl_df_data_example = os.path.join(_p_dir, "RomDataBu/tmp_csv")
print(g_project_kl_df_data_example)


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

#  ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊ 日志 end ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

g_plt_figsize = (14, 7)


def init_plot_set():
    """全局plot设置"""
    import seaborn as sns

    sns.set_context("notebook", rc={"figure.figsize": g_plt_figsize})
    sns.set_style("darkgrid")


init_plot_set()


print("aaaaaaaaaaaaaa")


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

import tempfile
from gtts import gTTS
from pygame import mixer

mixer.init()  # 初始化 mixer 物件

text = "找不到相關的維基百科資料"
lang = "zh-tw"


with tempfile.NamedTemporaryFile() as ntf:
    tts = gTTS(text=text, lang=lang)
    tts.save(f"{ntf.name}.mp3")
    mixer.music.load(f"{ntf.name}.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        pass

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
