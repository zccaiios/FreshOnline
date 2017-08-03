#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf.urls import url
from df_user import views

urlpatterns = [
    # 展示用户注册页面
    url(r'register/$', views.register),
    # 注册用户信息
    url(r'register_handle/$', views.register_handle),
    # 校验用户名是否已经被注册
    url(r'check_user_name_exist/$', views.check_username_exist),
]