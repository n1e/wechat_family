"""py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from LifeRiver import views as LR_VIEW

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LR_VIEW.index, name="index"),
    url(r'^index/', LR_VIEW.getLog, name="log"),
    url(r'^add/$', LR_VIEW.add, name="add"),
    url(r'^add/(\d+)/(\d+)/$', LR_VIEW.add_ext, name="add_ext"),
    url(r'^xx/(\d+)/(\d+)/$', LR_VIEW.jump, name="jump"),
    url(r'^upload/$', LR_VIEW.uploadPic), ]
