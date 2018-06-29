from django.db import models
from datetime import datetime


# 所属城市表
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name="城市")
    desc = models.CharField(max_length=200, verbose_name="描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 机构表
class CourseOrg(models.Model):
    ORG_CHOICES = (
        ("pxjg", "培训机构"),
        ("gx", "高校"),
        ("gr", "个人"),
    )
    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    category = models.CharField(max_length=20, choices=ORG_CHOICES, verbose_name="机构类别", default="pxjg")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(
        upload_to="org/%Y/%m",
        verbose_name="Logo",
        max_length=100)
    address = models.CharField(max_length=150, verbose_name="机构地址")
    # 一个城市里可能有很多机构，所以是一对多的关系
    city = models.ForeignKey(CityDict, verbose_name="所在城市", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    # 当学生点击学习课程，找到所属机构，学习人数加1
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    # 当发布课程就加1
    course_nums = models.IntegerField(default=0, verbose_name=u"课程数")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 教师表
class Teacher(models.Model):
    # 教师与机构同样是一对多关系
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE)
    age = models.IntegerField(default=18, verbose_name=u"年龄")
    name = models.CharField(max_length=50, verbose_name="教师名称")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    image = models.ImageField(
        default='',
        upload_to="teacher/%Y/%m",
        verbose_name=u"头像",
        max_length=100)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
