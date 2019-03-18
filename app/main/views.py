# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: views.py
# @Date:   2019-03-13 10:07:12
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-18 17:26:22

from flask import render_template, abort, request,jsonify, redirect,url_for,flash, current_app, send_from_directory
from . import main
from sqlalchemy import desc
from .. import db
from flask_login import login_user, logout_user, login_required,current_user
from ..models import User, Weidian
import os,json,time
from ..email import send_email
from .forms import JobDateForm
import json as simplejson
import requests
# from ops.task_scheduler_bak.josn import exec_shell
import subprocess
import json
import datetime
from datetime import date
from app.job.views import show_jobs,job_log
from ..models import TaskLog

######################################################################
@main.route('/')
#@login_required
def index():
    '''
    @note: 返回主页内容
    '''
    if not current_user.is_authenticated:
        return redirect('auth/login')
    else:
        task =  show_jobs()
        return render_template('all_job_list.html',task=task)

@main.route('/joblog')
def joblog():
    #job_log = job_log()
    #print (job_log)
    return render_template('all_job_log.html')

@main.route('/dellog',methods=['DELETE'])
def dellog():
    response = {}
    data = request.get_json(force=True)
    db_id = data.get('id')
    job_id = data.get('task_id')
    try:
        db.session.query(TaskLog).filter_by(id=db_id).delete()
        response['status']=True
        response['msg'] = "job [%s] joblog delete success!" % job_id
    except Exception as e:
        response["msg"] = "删除失败 --- %s" % e
        response['status'] = False    

   
    return jsonify(response)

@main.route('/createjob')
def createjob():
    #job_log = job_log()
    #print (job_log)
    return render_template('create_job.html')

# ######################################################################

def aps_test():
    print ('执行时间：{0}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
    return True

@main.route('/create/')
def add_job():
    #for i in range(5):
    print('[add job]: ',aps_test)
    current_app.apscheduler.add_job(func=aps_test, id="aps_test", trigger="interval", seconds=3, start_date="2019-3-14 13:39:00", end_date="2019-4-14 14:36:00")
    return 'ok'























@main.route('/delete_shop',methods=['POST','GET'])
def delete_shop():
    """从数据库中删除已经存在的主机"""
    weidian_id = json.loads(request.form.get('data'))['check_id']
    print (weidian_id)
    try:
        db.session.query(Weidian).filter(Weidian.id == weidian_id).delete()
        result = {'result': True, 'message': u"删除店铺成功" }
    except Exception as e:
        result = {'result': False, 'message': u"删除店铺失败,%s" % e}
    return jsonify(result)


@main.route('/about_me',methods=['POST','GET'])
def about_me():
    return render_template('about_me.html')



@main.route('/test',methods=['POST','GET'])
def test():
    return render_template('test.html')
