# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: config.py
# @Date:   2018-02-28 11:57:30
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-04-26 21:28:18
import os, logging
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
basedir = os.path.abspath(os.path.dirname(__file__))


# MySQL配置
mysql_info = dict(
    host = '127.0.0.1',
    port = 3306,
    dbname = 'jobs',
    username = 'root',
    password = 'guo.150019'
)

'''
    // setInterval( function () {
    //   t.ajax.reload(); // 刷新表格数据，分页信息不会重置
    // }, 5000 );
'''
MYSQL_URL = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8'%(mysql_info['username'],mysql_info['password'],
                                                           mysql_info['host'],mysql_info['port'],mysql_info['dbname'])

# apscheduler 配置
class TaskConfig(object):

    JOBS = [ ]
    SCHEDULER_JOBSTORES = {
        'default': SQLAlchemyJobStore(url=MYSQL_URL)
    }
    SCHEDULER_EXECUTORS = {
        # 'default': {'type': 'threadpool', 'max_workers': 20}
    }
    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 5
    }
    SCHEDULER_API_ENABLED = False
    

    # 任务日志
    log = logging.getLogger('apscheduler.executors.default')
    log.setLevel(logging.DEBUG)  # DEBUG
    fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    h = logging.StreamHandler()
    h = logging.FileHandler('/tmp/task_scheduler.log')

    h.setFormatter(fmt)
    log.addHandler(h)



    
class Config:
    """基本配置"""
    SQLALCHEMY_ECHO=False #用于显式地禁用或启用查询记录
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A0Zr98j/3yXR~XHH!jmN]LWX/,?RT'
    #SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    BABEL_DEFAULT_LOCALE = 'zh'
    # 公司邮箱域名后缀，限制只能公司域名才能注册
    COMPANY_MAIL_SUFFIX='sctux.com'
    # 用户注册功能开关: True:可注册；False: 关闭注册
    REGISTER = False
    
    # 邮件信息
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD =  os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = u'[TaskServices]'
    FLASKY_MAIL_SENDER = '2399447849@qq.com'
    FLASKY_ADMIN = '2399447849@qq.com' # os.environ.get('FANXIANG_ADMIN')

    #加密解密所需的key
    PRPCRYPTO_KEY= '2d4g53sdfs6L6K'



    # 配置类可以定义 init_app() 类方法，其参数是程序实例。
    # 在这个方法中，可以执行对当前 环境的配置初始化。
    # 现在，基类 Config 中的 init_app() 方法为空。
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = MYSQL_URL

    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + db_user + ':' + db_pass + '@' + db_host + '/' + db_name + '?charset=utf8mb4'

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = MYSQL_URL
    # DEMO_ENV=False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
