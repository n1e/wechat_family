# -*- coding :utf-8 -*-
from django.conf import settings as original_settings


def settings(request):
    return {'settings': original_settings}


def ip_add(request):
    return {'ip_add': request.META['REMOTE_ADDR']}