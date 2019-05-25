#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/25 17:31
from django.urls import path,include
from . import views as account_view

urlpatterns = [
    path("login/",account_view.auth_wx_login)
]