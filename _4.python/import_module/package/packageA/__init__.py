"""
__init__.py  放的東西
1. 包的初始化
2. 管理包接口
3. 包的信息, 版本, 作者
"""

__author__  = "David Wang <bunshue@gmail.com>"
__version__ = "1.0.5"
__date__    = "29 August 2025"
__status__  = "production"

# 使用相對導入(點開頭的導入), 引用moduleA.py的變數
# from . import moduleA
from .moduleA import xa
from .moduleB import xb
from .moduleC import xc

__all__ = ['xa', 'moduleA','xb', 'moduleB','xc', 'moduleC']

print('PackageA is imported')

__all__ = ['BASIC_FORMAT', 'BufferingFormatter', 'CRITICAL', 'DEBUG', 'ERROR',
           'FATAL', 'FileHandler', 'Filter', 'Formatter', 'Handler', 'INFO',
           'LogRecord', 'Logger', 'LoggerAdapter', 'NOTSET', 'NullHandler',
           'StreamHandler', 'WARN', 'WARNING', 'addLevelName', 'basicConfig',
           'captureWarnings', 'critical', 'debug', 'disable', 'error',
           'exception', 'fatal', 'getLevelName', 'getLogger', 'getLoggerClass',
           'info', 'log', 'makeLogRecord', 'setLoggerClass', 'warn', 'warning',
           'getLogRecordFactory', 'setLogRecordFactory', 'lastResort']


CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

