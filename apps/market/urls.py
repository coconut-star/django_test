from django.conf.urls import url
from apps.market import views


urlpatterns = [
    url(r'^$', views.market_depth),
    url(r'^customer/$', views.customer),
    url(r'^market_depth/$', views.market_depth)
]
