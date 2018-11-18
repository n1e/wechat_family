from django.conf.urls.defaults import *
from django.conf.urls import include,url
from LifeRiver import views as LR_VIEW

urlpatterns = [
    url('^/lr/$', LR_VIEW.getLog)
]