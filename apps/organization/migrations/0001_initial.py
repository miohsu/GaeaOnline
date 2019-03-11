# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-11 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='学校类别')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='城市')),
                ('desc', models.CharField(max_length=64, verbose_name='城市描述')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='学校名称')),
                ('desc', models.TextField(verbose_name='学校描述')),
                ('address', models.CharField(max_length=256, verbose_name='地址')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击量')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(max_length=128, upload_to='org/%Y/%m', verbose_name='logo')),
                ('tag', models.CharField(choices=[('Training Agency', '培训机构'), ('University', '高校'), ('Personal', '个人')], max_length=32, verbose_name='标签')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='organization.Category', verbose_name='类别')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='organization.City', verbose_name='所在城市')),
            ],
            options={
                'verbose_name': '学校',
                'verbose_name_plural': '学校',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='教师姓名')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('work_years', models.IntegerField(default=0, verbose_name='工作年限')),
                ('work_company', models.CharField(max_length=128, verbose_name='就职公司')),
                ('work_position', models.CharField(max_length=64, verbose_name='公司职位')),
                ('points', models.CharField(max_length=64, verbose_name='教学特点')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击量')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(max_length=128, upload_to='org/%Y/%m', verbose_name='logo')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='organization.School', verbose_name='所属机构')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
            },
        ),
    ]