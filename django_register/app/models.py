# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone as timezone
import datetime
import json


# 角色相关
#
class UserExt(models.Model):

    CHECKED_BOOL = [
        ('未验证', '未验证'),
        ('已验证', '已验证')
    ]

    SOURCE_CHOICE = [
        ('系统', '系统'),
        ('微信', '微信')
    ]

    user = models.ForeignKey(User, verbose_name='内建用户')
    openid = models.CharField(max_length=200, blank=True)
    user_name = models.CharField('用户名', max_length=20)
    head_img_url = models.CharField('头像', max_length=200)
    email = models.CharField('电子邮箱', max_length=20)
    checked_bool = models.CharField('邮箱验证', max_length=20, choices=CHECKED_BOOL)
    source = models.CharField('用户来源', max_length=20, choices=SOURCE_CHOICE)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.user_name + self.email
