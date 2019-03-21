# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: extensions.py
# @Date:   2019-03-05 18:02:51
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-21 10:52:00
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, AnonymousUserMixin
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
moment = Moment()

# task sevices
scheduler = APScheduler()

@login_manager.user_loader
def load_user(user_id):
    from ops.models import User
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
# login_manager.login_message = 'Your custom message'
login_manager.login_message_category = 'warning'

login_manager.refresh_view = 'auth.re_authenticate'
# login_manager.needs_refresh_message = 'Your custom message'
login_manager.needs_refresh_message_category = 'warning'


class Guest(AnonymousUserMixin):

    def can(self, permission_name):
        return False

    @property
    def is_admin(self):
        return False


login_manager.anonymous_user = Guest