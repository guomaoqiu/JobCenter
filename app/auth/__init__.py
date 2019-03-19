# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: __init__.py
# @Date:   2019-03-07 17:20:36
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-19 16:58:40
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
