import logging
import os
import sys
sys.path.append('..')


#项目路径
print (os.path.abspath(__file__))
#当前文件的绝对路径的上一级，__file__指当前文件
prj_path1 =  os.path.dirname(os.path.abspath(__file__))
prj_path = os.path.dirname(os.path.join(prj_path1))
#数据目录
data_path = os.path.join(prj_path,'Test_data')
#用例目录
test_path = os.path.join(prj_path,'Test_case')
#日志目录
log_file = os.path.join(prj_path,'log','log.txt')
report_file = os.path.join(prj_path,'report')

#log配置
logging.basicConfig(level=logging.DEBUG,    #日志级别
                    format = '[%(asctime)s] %(levelname)s [%(funcName]s: %(filename)s，%(lineno)d] %(message)s', #log格式
                    datefmt = '%Y-%m-%d %H:%M:%S',   #日期格式
                    filename =log_file,   # 日志输出文件
                    filemode = 'a')


#数据库配置
db_host = 'sh-cdbrg-50gjklty.sql.tencentcdb.com'
db_port = '60330'
db_user = 'root'
db_passwd = 'Anchnet!@123'                                                                                      )

