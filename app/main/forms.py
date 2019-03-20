# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: forms.py
# @Date:   2019-03-07 17:20:38
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-20 17:32:58

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,SelectField
from wtforms.validators import Required, Length, Email, DataRequired , EqualTo, Regexp

# NameForm
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

# JobDateForm
class JobDateForm(FlaskForm):
    job_id = StringField('任务名称',default="DATE-" , validators=[Required()])
    func_cmd = StringField('执行函数或命令', validators=[Required()])
    run_date = StringField('计划运行时间',default="2019-03-20 11:11:11", validators=[Required()])
    submit_date = SubmitField('确认添加')

# JobCronForm
class JobCronForm(FlaskForm):
    job_id = StringField('任务名称',default="CRON-" , validators=[Required()])
    func_cmd = StringField('执行函数或命令', validators=[Required()])
    cron_date = StringField('计划运行时间(秒 分 时 日 月 周)',default="20 10-15 11-15 * * *", validators=[Required()])
    submit_cron = SubmitField('确认添加')

# JobIntervalForm
class JobIntervalForm(FlaskForm):
    job_id = StringField('任务名称',default="INTERVAL-" , validators=[Required()])
    func_cmd = StringField('执行函数或命令', validators=[Required()])
    interval_time =  StringField('计划运行时间(秒 分 时 日 周)',default="10 0 0 0 0", validators=[Required()])
    #start_date = StringField('star_time(例如:2019-03-20 11:11:11)')
    #end_date = StringField('end_time')
    submit_interval = SubmitField('确认添加')    
