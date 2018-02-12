from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^register/$', views.user_register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^index/$', views.index, name='index'),
    url(r'^check_code/$', views.check_code, name='check_code'),
    url(r'^forget_password/$', views.forget_password, name='forget_password'),
]
