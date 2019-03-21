# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: test.py
# @Date:   2019-03-07 17:20:36
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-21 14:47:44
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask


def sensor():
    """ Function for test purposes. """
    print("Scheduler is alive!")

scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(sensor, 'interval', seconds=2)
scheduler.start()

app = Flask(__name__)


@app.route("/home")
def home():
    """ Function for test purposes. """
    return "Welcome Home :) !"


if __name__ == "__main__":
    app.run()