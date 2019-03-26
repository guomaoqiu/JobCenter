# -*- coding: utf-8 -*-
# @Author: guomaoqiu
# @File Name: webhook.py
# @Date:   2019-03-21 20:41:23
# @Last Modified by:   guomaoqiu
# @Last Modified time: 2019-03-22 18:38:18

'''
该脚本用于启动一个小web服务用于接收触发本地开发环境的代码push请求；
当本地代码提交后，通过设置的webhook功能触发该脚本
从而触发服务器仓库上面的代码执行git pull操作
以此达到自动热部署的目的
ps:服务端开启了debug功能功能所以可以热加载本地提交的变更操作。
'''

# 依赖包: pip install flask gitpython
from flask import Flask, request, jsonify,abort
import git, os

# 项目代码目录(相对于webhook.py这个脚本的路径)
code_dir = "./"

# 远程服务器代码地址
git_url = "git@github.com:guomaoqiu/JobCenter.git"

app = Flask(__name__)


@app.route('/pullcode', methods=['POST'])
def pullcode():
    if request.method == 'POST':
        print (request.headers)
        if os.path.isdir(code_dir):
            local_repo = git.Repo(code_dir)
            try:
                print (local_repo.git.pull())
                return jsonify({"result":True,"message":"pull success"})
            except Exception as e:
                return jsonify({"result":False,"message": "pull faild".format(e)})
        else:
            try:
                print (git.Repo.clone_from(url=git_url, to_path=code_dir))
                return jsonify({"result":True,"message":"clone success"})
            except Exception as e:
                return jsonify({"result":False,"message": "clone faild".format(e)})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)

# 服务端启动命令
#cd /home/JobCenter/ && nohup /root/.local/share/virtualenvs/JobCenter-OelQLIOn/bin/python /home/JobCenter/webhook.py >> /var/log/pullcode_JobCenter.log &
