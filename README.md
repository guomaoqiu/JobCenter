# 特点:
* 可视化界面操作
* 定时任务统一管理
* 完全兼容Crontab
* 支持秒级定时任务
* 任务可搜索、暂停、编辑、删除

# 用法:
```
$ git clone https://github.com/greyli/JobCenter.git
$ cd JobCenter
$ pipenv install --dev
$ pipenv shell
# 需提前创建数据库
$ flask init 

$ flask run
* Running on http://127.0.0.1:5000/
```

# 常用命令

```
$ pipenv install  # 创建虚拟环境并安装依赖
$ pipenv shell  # 激活虚拟环境
$ flask initdb  # 初始化数据库
$ flask admin  # 创建管理员账户
$ flask initdb --drop # 删除数据
```

## 平台登录界面
![](https://raw.githubusercontent.com/guomaoqiu/JobCenter/master/screenhots/login.jpg)

## 平台定时任务列表
![](https://raw.githubusercontent.com/guomaoqiu/JobCenter/master/screenhots/joblist.jpg)

## 平台定时任务日志
![](https://raw.githubusercontent.com/guomaoqiu/JobCenter/master/screenhots/loglist.jpg)



