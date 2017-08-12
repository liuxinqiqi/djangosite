#coding=utf-8
import logging



# logging
# 1.输出在终端
# 2.输出在文件
# critical>error>warning>info>debug  (默认打印warning以上信息)
#
#
# logging配置：
# logging.basicConfig(
#     level = logging.DEBUG,   #在debug等级以上
#     format = "%(asctime)s%(filename)s[line:%(lineno)d%(levelname)s%(message)s]",   #消息的输出格式
#     datemt = "%a,%d,%b,%Y,%H,%M,%S",  #指定日期时间的格式
#     filename = "test.log",   #日志的输出文件
#     filemode = "a"  #权限，w，写入，默认是a，追加
# )

logger = logging.getLogger()   #日志对象
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")  #输出格式对象

fh = logging.FileHandler('test1.log') #日志处理对象，表示向文件输出
ch = logging.StreamHandler()  #日志处理对象，表示向终端输出

fh.setFormatter(formatter)   #输出采用什么样的格式
ch.setFormatter(formatter)


#给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)


logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")


# format格式
# name, levelname, pathname, filename, module, funcName,
# lineno, created 当前时间
# asctime,
# thread,threadName
# process,processName
