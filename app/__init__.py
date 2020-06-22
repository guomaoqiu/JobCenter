# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: __init__.py
# @Date:   2019-03-05 18:37:34
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-26 18:05:07

from flask import Flask
from app.config import config, TaskConfig
import os,click
from app.extensions import bootstrap, db, login_manager, mail, moment,scheduler
from app.models import User,Role
from .main import main as main_blueprint
from .auth import auth as auth_blueprint
from .job import job as job_blueprint
from flask_debugtoolbar import DebugToolbarExtension

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')
  
    app = Flask(__name__)    
    
    app.config['SECRET_KEY'] = 'xxxxxxxxx'

    app.debug = False
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)

    # 配置引入
    app.config.from_object(config[config_name])
    app.config.from_object(TaskConfig())
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    # 上下文推送
    #app.app_context().push() 

    # 注册扩展
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    # 启动apscheduler服务
    scheduler.start()

    # apscheduler api认证
    @scheduler.authenticate
    def authenticate(auth):
        return auth['username'] == 'guest' and auth['password'] == 'guest'


    return app


# 注册扩展
def register_extensions(app):
    bootstrap.init_app(app)
    # db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    
    # toolbar.init_app(app)

    # task services

    # csrf.init_app(app)
    scheduler.init_app(app)

     
    db.init_app(app)

# 注册蓝图
def register_blueprints(app):
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(job_blueprint,url_prefix='/v1/cron/job')


# 注册命令
def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')

    @app.cli.command()
    def init():
        """Initialize Albumy."""
        click.echo('Initializing the database...')
        db.create_all()

        #click.echo('Initializing the roles and permissions...')
        Role.insert_roles()
        click.echo('Done.')
