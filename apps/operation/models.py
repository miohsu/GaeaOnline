from django.db import models
from django.contrib.auth import get_user_model

from courses.models import Course

User = get_user_model()
# Create your models here.

FAVORITE_CHOICES = (
    (1, '课程'),
    (2, '机构'),
    (3, '教师')
)


class UserConsult(models.Model):
    name = models.CharField(max_length=32, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    course = models.ForeignKey(Course, related_name='consult', verbose_name='课程名')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseComment(models.Model):
    user = models.ForeignKey(User, related_name='comments', verbose_name='用户')
    course = models.ForeignKey(Course, related_name='comments', verbose_name='课程')
    comment = models.CharField(max_length=256, verbose_name='评论')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment


class UserFavorite(models.Model):
    user = models.ForeignKey(User, related_name='favorite', verbose_name='用户')
    fav_id = models.IntegerField(default=0, verbose_name='具体ID')
    fav_type = models.IntegerField(choices=FAVORITE_CHOICES, verbose_name='收藏类型')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}-{}-{}".format(self.user, self.fav_type, self.fav_id)


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name='接收用户')
    message = models.CharField(max_length=512, verbose_name='消息')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourse(models.Model):
    user = models.ForeignKey(User, related_name='courses', verbose_name='用户')
    course = models.ForeignKey(Course, related_name='users', verbose_name='课程')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}-{}".format(self.user.name, self.course.name)
