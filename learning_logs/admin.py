from django.contrib import admin

# Register your models here.
# 导入要注册的模型
from learning_logs.models import Topic, Entry
# 让Django通过管理网站管理模型
admin.site.register(Topic)
admin.site.register(Entry)