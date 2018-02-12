# -*- coding: utf-8 -*-
from app.models import UserExt


def is_valid(request):
    # 判断是否是存在的用户端用户

    email = request.POST['email']
    try:
        user_ext = UserExt.objects.get(email=email)
        return user_ext.user, u''
    except Exception as e:
        print (e, '[<-- is_valid -->] in user_ext.py')
        return None, u'该用户不存在'

