'''定义learning_logs的URL模式'''
from django.conf.urls import url

from . import views

urlpatterns = [
	#homepage
	url(r'^$',views.index,name = 'index'),
	#topics
	url(r'^topics/$',views.topics,name = 'topics'),
	#特定主题的详细页面
	url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name = 'topic'),
	#用于添加新主题的网页
	url(r'^new_topic/$',views.new_topic,name = 'new_topic'),
	#用于添加新条目的页面
	url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
	#用户修改条目的页面
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
		name='edit_entry'),
]