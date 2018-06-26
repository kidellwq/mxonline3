# Generated by Django 2.0.6 on 2018-06-27 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='按时交作业,不然叫家长', max_length=300, verbose_name='老师告诉你'),
        ),
        migrations.AddField(
            model_name='course',
            name='you_need_know',
            field=models.CharField(default='一颗勤学的心是本课程必要前提', max_length=300, verbose_name='课程须知'),
        ),
    ]
