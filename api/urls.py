#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/5/25 17:34
from django.urls import path,include

urlpatterns = [
    path("account/",include('api.Account.urls')),
]
