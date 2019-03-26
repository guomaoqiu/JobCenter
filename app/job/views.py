# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: views.py
# @Date:   2019-03-12 17:28:21
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-26 16:50:33

from . import job
from .. import scheduler
from flask import request, jsonify, Response
import json
from .. import db
from ..models import TaskLog
from flask_login import login_required

from .public import DateEncoder
from .core import jobfromparm, get_job_logs

@job.route('/pause',methods=['POST'])
@login_required
def pause_job():
    '''暂停作业'''
    print(request)
    response = {'status': False}
    try:
        data = request.get_json(force=True)
        print (data)
        job_id = data.get('id')
        print(job_id)
        scheduler.pause_job(job_id)
        response['msg'] = "job[%s] pause success!"%job_id
        response['status'] = True
    except Exception as e:
        response['msg'] = str(e)
    return jsonify(response)
 

@job.route('/resume',methods=['POST'])
@login_required
def resume_job():
    '''恢复作业'''
    response = {'status': False}
    try:
        data = request.get_json(force=True)
        job_id = data.get('id')
        scheduler.resume_job(job_id)
        response['msg'] = "job[%s] resume success!"%job_id
        response['status'] = True
    except Exception as e:
        response['msg'] = str(e)
    return jsonify(response)

@job.route('/remove',methods=['DELETE'])
@login_required
def reomve_jobs():
    '''删除作业'''
    response = {'status': False}
    try:
        data = request.get_json(force=True)
        job_id = data.get('id')
        if job_id != 'all':
            scheduler.remove_job(job_id)
            response['msg'] = "job [%s] remove success!"%job_id
        else:
            scheduler.remove_all_jobs()
            response['msg'] = "job all remove success!"
        response['status'] = True
    except Exception as e:
        response['msg'] = str(e)
    return jsonify(response)

@job.route('/edit', methods=['POST'])
@login_required
def edit_job():
    '''修改作业'''
    response = {'status': '-1'}
    try:
        data = request.get_json(force=True)
        job_id = data.get('id')
        old_job = scheduler.get_job(job_id)
        if old_job:
            jobfromparm(scheduler,**data)
            response['status'] = 0
            response['message'] = "job[%s] edit success!"%job_id
        else:
            response['message'] = "job[%s] Not Found!"%job_id
    except Exception as e:
        response['message'] = str(e)
    return json.dumps(response)

@job.route('/add', methods=['POST'])
@login_required
def add_job():
    '''新增作业'''
    response = {'status': '-1'}
    try:
        data = request.get_json(force=True)
        print (data)
        job_id = jobfromparm(scheduler,**data)
        print (job_id)    
        response['status'] = 0
        response['msg'] = "job [%s] add success!"%job_id
        response['result'] = True
    except Exception as e:
        response['msg'] = str(e)
        print(e)
    return jsonify(response)    

@job.route('/show_jobs/', methods=['GET'])
@login_required

def show_jobs():
    '''获取所有jobs信息'''
    response = {}
    try:
        # 获取单个计划任务详情，如果有传入id则为单个；否则为所有
        jid = request.args.get('id')
        if jid == None:
            ret_list = scheduler.get_jobs()

        else:
            ret_list = [scheduler.get_job(jid)]
        info_list = []

        for ret in ret_list:

            # 判断任务类型是否为 cron
            if  "cron" in str(ret.trigger):
                cron = {}
                fields = ret.trigger.fields
                for field in fields:
                    
                    cron[field.name] = str(field)
                cron_list = [cron['second'],cron['minute'],cron['hour'],cron['day'],cron['month'],cron['day_of_week']]
                info = {
                    'id':ret.id,
                    'next_run_time':ret.next_run_time,
                    'cmd':ret.kwargs.get('cmd'),
                    'func':ret.func_ref,
                    'status':"<p style='background-color:#46c37b;color:#525151;padding:3px 5px;border-radius:5px;font-weight:bold'>Runing...</p>" \
                             if ret.next_run_time != None else \
                             "<p style='background-color:#f0a63a;color:#525151;padding:3px 5px;border-radius:5px;font-weight:bold'>Pause...</p>",
                    'cron':' '.join(cron_list)
                }
                info_list.append(info)  


            # 判断任务类型是否为 date    
            if "date" in str(ret.trigger):
                info = {

                    'id':ret.id,
                    'next_run_time':ret.next_run_time,
                    'cmd':ret.kwargs.get('cmd'),
                    'func':ret.func_ref,
                    'status':"<p style='background-color:#46c37b;color:#525151;padding:3px 5px;border-radius:5px;font-weight:bold'>Runing...</p>" \
                             if ret.next_run_time != None else \
                             "<p style='background-color:#f0a63a;color:#525151;padding:3px 5px;border-radius:5px;font-weight:bold'>Pause...</p>",
                    'cron': ret.trigger.run_date
                }
                info_list.append(info)

             # 判断任务类型是否为 interval
            if "interval" in str(ret.trigger):
                #print (ret.kwargs.get("end_date"))
                #fields = ret.kwargs
                timedelta_seconds = ret.trigger.interval_length
                #print(type(fields))
                info = {
                    'id':ret.id,
                    'next_run_time':ret.next_run_time,
                    'cmd':ret.kwargs.get('cmd'),
                    'func':ret.func_ref,
                    'status':"<p style='background-color:#46c37b;color:#525151;padding:3px 5px;border-radius:5px;font-weight:bold'>Runing...</p>" \
                             if ret.next_run_time != None else \
                             "<p style='background-color:#f0a63a;color:#525151;padding:3px 5px;border-radius:5px;font-weight:bold'>Pause...</p>",
                    'cron': str(ret.trigger.interval_length) + "s / run"
                }
                info_list.append(info)
        #print(info_list)        
        response['status'] = True
        response['data'] = info_list
        response['count'] = len(info_list)
       
    except Exception as e:
        response['msg'] = str(e)
    result = json.dumps(response,cls=DateEncoder)

    return result

@job.route('/job_log', methods=['GET'])
@login_required
def job_log():
    '''获取所有job log信息'''
    response = {}
    try:
        db_id = request.args.get('id')
        if db_id != None:
            result = db.session.query(TaskLog).filter_by(id=db_id).first()
            ret = result.to_json()['stdout']
            return jsonify({"stdout": ret})
        else:    
            ret = get_job_logs(request.args)
        response['status'] = 0
        response['data'] = ret
        response['count'] = len(ret)
    except Exception as e:
        response['msg'] = str(e)

    return json.dumps(response,cls=DateEncoder)