from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


DEGREE_CHOICES = (
    ('beginner', '初级'),
    ('intermediate', '中级'),
    ('advanced', '高级'),
)


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='类别')

    class Meta:
        verbose_name = '课程类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=128, verbose_name='课程名称')
    desc = models.CharField(max_length=256, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(max_length=16, choices=DEGREE_CHOICES, verbose_name='难度')
    study_time = models.IntegerField(default=0, verbose_name='学习时长')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='course/%Y/%m', max_length=128, verbose_name='封面图')
    click_nums = models.IntegerField(default=0, verbose_name='点击量')
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    tag = models.CharField(max_length=64, default='', verbose_name='课程标签')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Chapter(models.Model):
    course = models.ForeignKey(Course, related_name='chapters', verbose_name='课程')
    name = models.CharField(max_length=128, verbose_name='章节')
    study_time = models.IntegerField(default=0, verbose_name='学习时长')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='video', verbose_name='章节')
    name = models.CharField(max_length=128, verbose_name='视频')
    study_time = models.IntegerField(default=0, verbose_name='学习时长')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '课程视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, related_name='resources', verbose_name='课程')
    name = models.CharField(max_length=128, verbose_name='资源名称')
    download = models.FileField(max_length=128, upload_to='course/resource/%Y/%m', verbose_name='资源文件')
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
