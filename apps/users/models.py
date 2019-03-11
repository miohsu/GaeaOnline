from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENDER_CHOICES = (
    ('male', '男'),
    ('female', '女'),
)

SEND_TYPE_CHOICES = (
    ('register', '注册'),
    ('forget', '找回密码'),
)


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=64, default='', verbose_name='昵称')
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES, null=True, blank=True, verbose_name='性别')
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')
    address = models.CharField(max_length=128, default='', verbose_name='地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机')
    image = models.ImageField(max_length=128, upload_to='image/%Y/%m', default='image/default.png', verbose_name='头像')

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=8, verbose_name='验证码')
    email = models.EmailField(max_length=64, verbose_name='邮箱')
    send_type = models.CharField(max_length=16, choices=SEND_TYPE_CHOICES, verbose_name='验证码类型')
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}({})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题')
    image = models.ImageField(max_length=128, upload_to='banner/%Y/%m', verbose_name='轮播图')
    url = models.URLField(max_length=256, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='上传时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
