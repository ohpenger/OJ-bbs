# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    head_sculpture = models.ImageField(null=True, blank=True, verbose_name=u'头像')
    sex = models.CharField(max_length=5, verbose_name=u'性别')
    born_date = models.DateField(verbose_name=u'生日')

    class Meta(AbstractUser.Meta):
        pass
