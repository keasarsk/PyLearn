"""skweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
from django.conf.urls import url

def login(request):
    '''
    处理用户请求并返回同容
    :param request:用户请求相关的所有信息
    :return:
    '''

    # HttpResponse功能只返回字符串
    # return HttpResponse('skkkkkk')

    # render可以返回文件内容
    return render(request,'skweb.html')
urlpatterns = [
    path('admin/', admin.site.urls),
#   自己写path    ??????不好使
#     path('admin/', login),
#     url(r'^login/',login),

]
