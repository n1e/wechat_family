# coding:utf-8
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from LifeRiver.models import Log
from LifeRiver.models import LRPic
from PIL import Image
# Create your views here.


def index(request):
    #return HttpResponse(u'傻了吧')
    return render(request, 'Log.html')


def getLog(request):
    logs = Log.objects.all()
    '''
    t = loader.get_template("Log.html")
    c = Context({'Logs': logs, 'Lists': range(1, 1), })
    return HttpResponse(t.render(c))
    '''
    return render(request, 'Log.html', {'Logs': logs, 'Lists': range(1, 1), })
    ###return render(request, 'Log.html')


def add(request):
    num1 = request.GET['a']
    num2 = request.GET['b']
    res = int(num1) + int(num2)
    return HttpResponse('result is %s' % str(res))


def add_ext(request, a, b):
    num = int(a) + int(b)
    return HttpResponse('result is %s' % str(num))


def jump(request, a, b):
    return HttpResponseRedirect(
        reverse('add_ext', args=(a, b))
    )


def uploadPic(request):
    print 'into uploadPic'
    if request.method == 'POST':
        img = LRPic(image=request.FILES.get('img'), title='测试')
        img.save()
    return HttpResponseRedirect(
        reverse('log'))
