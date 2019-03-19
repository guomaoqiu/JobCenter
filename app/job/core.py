# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: core.py
# @Date:   2019-03-13 10:20:38
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-19 16:58:51

from .public import exec_shell
from ..models import TaskLog
from .. import db, scheduler

def exe_cmd(cmd,task_id):
    '''执行CMD命令'''
 
    with scheduler.app.app_context():
        recode, stdout = exec_shell(cmd)
        data = dict(
            task_id = task_id,
            status = True if recode == 0 else False,
            cmd = cmd,
            stdout = stdout
        )
        #print (current_app.name)
        new_log = TaskLog(**data)
        try:
            db.session.add(new_log)
            db.session.commit()
            print("任务日志写入成功")

        except Exception as e:
            print("任务日志写入失败 - %s" % e)

        if recode != 0:
            print('[Error] (%s---[%s]) failed'%(cmd,task_id))
            exit(407)
        print('[Success] (%s---[%s]) success'%(cmd,task_id))
        return stdout


import time
def aps_test():
    print ('执行时间：{0}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
    return True

def jobfromparm(scheduler,**jobargs):
    """
    "date": 是最基本的一种调度，作业任务只会执行一次。它表示特定的时间点触发。
     http://127.0.0.1:5000/v1/cron/job/add   
   {
        "id": "once6",
        "cmd": "echo '麻痹'",
        "run_date": "2019-03-13 18:05:00",
        "trigger_type": "date"
    }


    “interval": 固定时间间隔触发。interval 间隔调度




    "cron": 在特定时间周期性地触发，和Linux crontab格式兼容。它是功能最强大的触发器。
    """
    id = jobargs['id']
    func=__name__+':'+'exe_cmd'
    args = jobargs['cmd']
    trigger_type = jobargs['trigger_type']

    if trigger_type == "date":
        run_date = jobargs['run_date']
        scheduler.add_job(func=func, id=id, kwargs={'cmd':args,'task_id':id}, trigger='date' ,run_date=run_date, replace_existing=True)
        print("添加一次性任务成功---[ %s ] " % id)
        return id

    elif trigger_type == "interval":
        #start_date = jobargs['start_date']
        #end_date = jobargs['end_date']
        

        # scheduler.add_job(func=aps_test, id=id, kwargs={'cmd':args,'task_id':id}, 
            # trigger='interval', seconds=30,start_date=start_date, end_date=start_date, replace_existing=True,)
        #scheduler.add_job(func=aps_test, id=id, trigger='interval',start_date=start_date, end_date=start_date, replace_existing=True,)
        scheduler.add_job(func=func, id=id, kwargs={'cmd':args,'task_id':id},trigger='interval',seconds=5,  replace_existing=True)


        print("添加间隔任务成功---[ %s ] " % id)
        return id

    elif trigger_type == "cron":
        cron = jobargs['cron'].split(' ')
        cron_rel = dict(second=cron[0], minute=cron[1], hour=cron[2], day=cron[3], month=cron[4], day_of_week=cron[5])
        scheduler.add_job(func=func,id=id, kwargs={'cmd':args,'task_id':id},trigger='cron',**cron_rel,replace_existing=True)
        print("添加周期执行任务成功任务成功---[ %s ] " % id)
        return id
    else:
        pass
    
    

def get_job_logs(args):
    jid = args.get('id')
    pageNum = int(args.get('pageNum',1))
    pageSize = int(args.get('pageSize',25))
    if jid == None:
        data_list = TaskLog.query.order_by(TaskLog.id.desc()).paginate(
            pageNum, pageSize, error_out=False
        )
        total = data_list.total
        data_list = data_list.items
    else:
        data_list = TaskLog.query.filter_by(task_id=jid).all()
    ret_list = []
    for data in data_list:
        ret_list.append(data.to_json())
    return ret_list