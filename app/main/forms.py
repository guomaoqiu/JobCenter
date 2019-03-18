# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: forms.py
# @Date:   2019-03-07 17:20:38
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-15 15:56:28

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import Required, Length, Email, DataRequired , EqualTo, Regexp

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')





# 一次性任务表单
class JobDateForm(FlaskForm):
    # wechat_name = StringField('您的微信群昵称?', validators=[Required()])
    job_id = StringField('任务名称', validators=[Required()])
    run_date = StringField('运行时间', validators=[Required()])
    submit = SubmitField('提交')