# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from libs.tools import args_required
from django.conf import settings
import time
from app.models import *


# 用户注册
@args_required('POST', 'email', 'password')
def register(request):

    email = request.POST['email']
    password = request.POST['password']

    try:
        user = User.objects.create_user(
            username=email,
            password=password,
            email=email
        )

    except Exception as e:
        print (e, '[<-- register -->] in user.py')
        return False, u'该账号已注册'

    now_time = int(round(time.time() * 1000))
    username = u'用户_' + str(now_time)

    UserExt.objects.create(
        user=user,
        user_name=username,
        email=email,
        head_img_url=settings.MEDIA_URL + 'default-user.png')

    return True, u'注册成功'


def is_valid(request, user):
    # 用于验证用户端用户

    post = request.POST
    user = authenticate(username=user.email,
                        password=post['password'])
    return user


# def forget_pass(request):
#     """
#
#     :param request:
#     :return:
#     3:该用户未注册
#     """
    # phone = request.POST.get('phone', '')
    # if not phone:
    #     return HttpResponse(3)
    # try:
    #     user_ext = UserExt.objects.get(phone=phone)
    # except:
    #     return HttpResponse(3)
    # if not user_ext:
    #     return HttpResponse(3)
    # return send_verify(request)


@args_required('POST', 'email', 'password')
def set_password(request):
    email = request.POST.get('email')
    new_password = request.POST.get('password')

    try:
        user_ext = UserExt.objects.get(email=email)

    except Exception as e:
        print (e, '[<-- register -->] in user.py')
        return False, u'该账号不存在'

    if not new_password:
        return False, u"请输入正确的新密码"

    user_ext.user.set_password(new_password)
    user_ext.user.save()
    return True, u"修改密码成功, 请重新登录"
