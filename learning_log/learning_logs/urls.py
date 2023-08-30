from django.urls import path, re_path
from . import views
# from django.conf.urls import url

app_name = 'learning_logs'

urlpatterns =[#主页
    path('', views.index, name='index'),
    #显示所有主题
    path('topics/', views.topics, name='topics'),

    re_path("topics/(?P<topic_id>\d+)/", views.topic, name='topic'),
    # 用于添加新主题网页
    path("new_topic/", views.new_topic, name='new_topic'),
    path("new_entry/(?P<topic_id>\d+)/", views.new_entry, name='new_entry'),
    path('edit_entry/(?P<entry>id>\d+/',views.edit_entry, name= 'edit_entry'),
]