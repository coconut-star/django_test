from django.conf.urls import url
from apps.hedgetrade import views


urlpatterns = [
    url(r'^$', views.dashboard),
]