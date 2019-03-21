# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: errors.py
# @Date:   2019-03-07 17:20:38
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-21 14:49:46

from flask import render_template
from . import main


@main.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
