# -*- coding:utf-8 -*-
# 依赖包: pip install flask gitpython
from flask import Flask, request, jsonify,abort
import git, os,commands
# 远程服务器代码地址
code_dir = "./"
# 远程仓库地址
git_url = "git@gitee.com:demo_demo/weidian_collection.git"

#白名单
#allow_ip=[""]
app = Flask(__name__)

restart_services = commands.getoutput("systemctl restart supervisord && echo 'restart supervisord success......'")

@app.route('/pullcode', methods=['POST'])
def pullcode():

    # 只允许指定服务器向Flask应用发起POST请求，否则直接返回403
    #if request.headers.get('X-Forwarded-For', request.remote_addr) not in allow_ip:
    #    return abort(403)
    if request.method == 'POST':
        print request.headers
        if os.path.isdir(code_dir):
            local_repo = git.Repo(code_dir)
            try:
                print local_repo.git.pull()
                # 重新加载代码、重启服务
                restart_services
                return jsonify({"result":True,"message":"pull success"})
            except Exception,e:
                return jsonify({"result":False,"message": "pull faild".format(e)})
        else:
            try:
                print git.Repo.clone_from(url=git_url, to_path=code_dir)
                # 重新加载代码、重启服务
                restart_services
                return jsonify({"result":True,"message":"clone success"})
            except Exception, e:
                return jsonify({"result":False,"message": "clone faild".format(e)})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008)