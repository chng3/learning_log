# learning_log
python 从入门到实践 第十八章项目
## 18章

### issue 1
执行 python manage.py migrate 创建数据库时，出现报错：
SyntaxError: Generator expression must be parenthesized

通过搜索发现是从 python3.7开始 Django 要就的最低版本是 1.11.17 ，书中的环境好像是 python 3.4 还是 3.5 版本，本地的环境是 3.9 的，所以我打算直接安装 Django 2.0

具体原因看：https://stackoverflow.com/questions/51265858/syntaxerror-generator-expression-must-be-parenthesized

通过安装 Django2.0版本

```
 pip3 install django==2.0
```

 安装后，重新执行创建数据库命令成功！！

### issue 2
在 learning_log 文件夹下编写 urls.py 文件时，当添加包含模块 learning_logs 
```
url(r'', include('learning_logs.urls', namespace='learning_logs'))
```
出现 Specifying a namespace in include() without providing an app_name is not supported. Set the app_name attribute in the included module, or pass a 2-tuple containing the list of patterns and app_name instead. 报错
解决方式是改写为
```
url(r'', include(('learning_logs.urls','learning_logs'), namespace='learning_logs')),
```
帮助链接：https://stackoverflow.com/questions/48608894/improperlyconfigurederror-about-app-name-when-using-namespace-in-include
### 笔记
每当需要修改”学习笔记“管理的数据时，都需要 1.修改models.py 2.对learning_logs调用makemigrations，让Django迁移项目

## 19章 让用户可以新建主题、创建条目、编辑条目

### 新建主题 issue 1
完成创建新条目的关键代码后，运行出现 No module named 'django.core.urlresolvers' 报错，发现是django2版本中已经移除了这个模组，搬到了django.url，应该改写成
```
from django.urls import reverse
```
问题链接：https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers

