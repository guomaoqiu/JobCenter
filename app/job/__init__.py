# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: __init__.py
# @Date:   2019-03-12 17:30:33
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-16 19:50:41

# 注册蓝本 必须用下列顺序 避免陷入循环依赖
from flask import Blueprint
job = Blueprint('job', __name__)

from . import views, core