# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: forms.py
# @Date:   2019-03-07 17:20:38
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-20 10:41:24

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,SelectField
from wtforms.validators import Required, Length, Email, DataRequired , EqualTo, Regexp

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


# 一次性任务表单
class JobDateForm(FlaskForm):
    # wechat_name = StringField('您的微信群昵称?', validators=[Required()])
    job_id = StringField('任务名称',default="DATE-" , validators=[Required()])
    func_cmd = StringField('执行函数或命令', validators=[Required()])
    run_date = StringField('计划运行时间',default="2019-03-20 11:11:11", validators=[Required()])
    submit_date = SubmitField('确认添加')


class JobCronForm(FlaskForm):
    # wechat_name = StringField('您的微信群昵称?', validators=[Required()])
    job_id = StringField('任务名称',default="CRON-" , validators=[Required()])
    func_cmd = StringField('执行函数或命令', validators=[Required()])
    cron_date = StringField('计划运行时间(秒 分 时 日 月 周)',default="* * * * * *", validators=[Required()])
    submit_cron = SubmitField('确认添加')

class JobIntervalForm(FlaskForm):
    # wechat_name = StringField('您的微信群昵称?', validators=[Required()])
    job_id = StringField('任务名称',default="INTERVAL-" , validators=[Required()])
    func_cmd = StringField('执行函数或命令', validators=[Required()])
    select = SelectField("间隔周期",choices=[('w',"周"),('d',"天"),('h','时'),('m',"分"),('s','秒')])
    interval_num = StringField("间隔数值", validators=[Required()])

    start_date = StringField('star_time',default="2019-03-20 11:11:11", validators=[Required()])
    end_date = StringField('end_time',default="2019-03-20 11:11:11", validators=[Required()])
    submit_interval = SubmitField('确认添加')    
