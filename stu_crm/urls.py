from django.conf.urls import patterns, url
from stu_crm import views

urlpatterns = [
    url(r'^$', views.index, name="index")
]