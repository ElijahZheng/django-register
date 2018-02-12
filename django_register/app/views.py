from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import libs.CheckCode
from app.models import *
import app.user, app.user_ext
import json


def user_register(request):
    if request.method == 'POST':

        check_code = request.POST.get('check_code')

        # 获取通过 checkcode函数获取保存到 session的验证码字符串
        session_code = request.session["check_code"]

        # 将用户输入的验证码 与后台session验证码 做比对：
        if check_code.strip().lower() != session_code.lower():
            return render(request, 'app/register.html',
                          {'msg': '验证码不匹配'})

        ok, msg = app.user.register(request)
        if not ok:
            return render(request, 'app/register.html',
                          {'msg': msg})

        user, msg = app.user_ext.is_valid(request)
        dj_login(request, user)
        return HttpResponseRedirect("/app/index")

    return render(request, 'app/register.html')


def index(request):
    try:
        user_ext = UserExt.objects.get(user=request.user)
    except:
        user_ext = None

    data = {
        'user_ext': user_ext
    }
    return render(request, 'app/index.html', data)


def user_login(request):
    if request.method == 'POST':

        check_code = request.POST.get('check_code')

        # 获取通过 checkcode函数获取保存到 session的验证码字符串
        session_code = request.session["check_code"]

        # 将用户输入的验证码 与后台session验证码 做比对：
        if check_code.strip().lower() != session_code.lower():
            return render(request, 'app/login.html',
                          {'msg': '验证码不匹配'})

        user, msg = app.user_ext.is_valid(request)
        if user is None:
            return render(request, 'app/login.html', {'msg': msg})  # 不存在用户

        if app.user.is_valid(request, user) is None:
            return render(request, 'app/login.html', {'msg': u'用户名或密码错误'})

        dj_login(request, user)

        return HttpResponseRedirect("/app/index")

    return render(request, 'app/login.html')


def forget_password(request):
    if request.method == 'POST':

        check_code = request.POST.get('check_code')

        # 获取通过 checkcode函数获取保存到 session的验证码字符串
        session_code = request.session["check_code"]

        # 将用户输入的验证码 与后台session验证码 做比对：
        if check_code.strip().lower() != session_code.lower():
            return render(request, 'app/forget_password.html',
                          {'msg': '验证码不匹配'})

        ok, msg = app.user.set_password(request)
        if not ok:
            return render(request, 'app/forget_password.html', {'msg': msg})

        return render(request, 'app/login.html', {'msg': msg})

    return render(request, 'app/forget_password.html')


def user_logout(request):
    dj_logout(request)
    return HttpResponseRedirect('/app/login')


# 验证码
def check_code(request):

    # 调用gene_code函数生成验证字符串，生成验证码图片的数据流（二进制格式）
    img_str, img_data = libs.CheckCode.gene_code()

    # 将验证码（字符串）保存到session中，以便login函数可以调用
    request.session["check_code"] = img_str

    # 将验证码图片以文件流的形式返回，然后前端通过<img src="/your_url/">就可以读取到图片了

    return HttpResponse(img_data)
