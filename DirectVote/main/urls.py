#-*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/submit', views.loginSubmit, name='main.loginSubmit'),
    url(r'^login', views.loginUser, name='main.loginUser'),
    url(r'^logout', views.logoutUser, name='main.logoutUser'),
    url(r'^view/proposals', views.proposals_page, name='main.proposals_page'),
    url(r'^view/(?P<page>[\w,\s-]+$)$', views.viewPage, name='main.viewPage'),
    url(r'', views.home, name='main.home'),
]
