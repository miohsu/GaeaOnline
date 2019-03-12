from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

TAG_CHOICES = (
    ('Training Agency', '培训机构'),
    ('University', '高校'),
    ('Personal', '个人'),
)


class City(models.Model):
    name = models.CharField(max_length=32, verbose_name='城市')
    desc = models.CharField(max_length=64, verbose_name='城市描述')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='学校类别')

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=64, verbose_name='学校名称')
    desc = models.TextField(verbose_name='学校描述')
    category = models.ForeignKey(Category, related_name='schools', verbose_name='类别')
    address = models.CharField(max_length=256, verbose_name='地址')
    city = models.ForeignKey(City, related_name='schools', verbose_name='所在城市')
    click_nums = models.IntegerField(default=0, verbose_name='点击量')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='org/%Y/%m', max_length=128, verbose_name='logo')
    tag = models.CharField(max_length=32, choices=TAG_CHOICES, verbose_name='标签')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '学校'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=32, verbose_name='教师姓名')
    age = models.IntegerField(null=True, blank=True, verbose_name='年龄')
    school = models.ForeignKey(School, related_name='teachers', verbose_name='所属机构')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=128, verbose_name='就职公司')
    work_position = models.CharField(max_length=64, verbose_name='公司职位')
    points = models.CharField(max_length=64, verbose_name='教学特点')
    click_nums = models.IntegerField(default=0, verbose_name='点击量')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='org/%Y/%m', max_length=128, verbose_name='logo')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
