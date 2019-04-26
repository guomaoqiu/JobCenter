![](https://blog.sctux.com/2019/03/19/Flask%E7%BB%93%E5%90%88APScheduler%E5%AE%9E%E7%8E%B0%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E6%A1%86%E6%9E%B6%E5%B9%B3%E5%8F%B0/info.png)




# 特点:
* 可视化界面操作
* 定时任务统一管理
* 完全兼容Crontab
* 支持秒级定时任务
* 作业任务可搜索、暂停、编辑、删除
* 作业任务持久化存储、三种不同触发器类型作业动态添加

<a href="http://jobcenter.sctux.com/" target="_blank">
  <img src="https://img.alicdn.com/tfs/TB12GX6zW6qK1RjSZFmXXX0PFXa-744-122.png" width="180" />
</a>

(注: demo版本部分功能已禁用🍺)

# 用法:
```
$ git clone https://github.com/guomaoqiu/JobCenter.git
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
## APScheduler工作流程图
![](https://blog.sctux.com/2019/03/19/Flask%E7%BB%93%E5%90%88APScheduler%E5%AE%9E%E7%8E%B0%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E6%A1%86%E6%9E%B6%E5%B9%B3%E5%8F%B0/liuchengtu.png)

## 清爽的登录界面
![](https://blog.sctux.com/2019/03/19/Flask%E7%BB%93%E5%90%88APScheduler%E5%AE%9E%E7%8E%B0%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E6%A1%86%E6%9E%B6%E5%B9%B3%E5%8F%B0/login.png)

## 针对不同触发器动态增加定时任务
![](https://blog.sctux.com/2019/03/19/Flask%E7%BB%93%E5%90%88APScheduler%E5%AE%9E%E7%8E%B0%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E6%A1%86%E6%9E%B6%E5%B9%B3%E5%8F%B0/addjob.png)

## 任务执行输出日志持久化存放并展示
![](https://blog.sctux.com/2019/03/19/Flask%E7%BB%93%E5%90%88APScheduler%E5%AE%9E%E7%8E%B0%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E6%A1%86%E6%9E%B6%E5%B9%B3%E5%8F%B0/stdout.png)

## 任务列表中暂停、恢复已添加定时任务
![](https://blog.sctux.com/2019/03/19/Flask%E7%BB%93%E5%90%88APScheduler%E5%AE%9E%E7%8E%B0%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E6%A1%86%E6%9E%B6%E5%B9%B3%E5%8F%B0/pausejob.png)


