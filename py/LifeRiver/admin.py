# -!- coding:utf-8 -!-
from django.contrib import admin
from LifeRiver import models as lr_models
# Register your models here.


class LogAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(LogAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            print 'debug'
            return qs


admin.site.register(lr_models.Log, LogAdmin)#, lr_models.LogList
#向admin中注册管理