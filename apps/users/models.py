from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# 定义用户表，UserProfile继承Django的User字段
class UserProfile(AbstractUser):
    # 性别选项
    GENDER_CHOICES = (
        ("male", "男"),
        ('female', "女")
    )
    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    # 出生日期
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    # 性别
    gender = models.CharField(
        max_length=6,
        verbose_name="性别",
        choices=GENDER_CHOICES,
        default="female"
    )
    # 地址
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 电话
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 头像，需安装pollow库
    image = models.ImageField(
        upload_to="image/%Y/%m",
        default="image/default.png",
        max_length=100,
        verbose_name="头像"
    )

    # Meta选项，后台显示名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 打印方法
    def __str__(self):
        return self.username

    def unread_nums(self):
        from operation.models import UserMessage
        return UserMessage.objects.filter(has_read=False, user=self.id).count()


# 邮箱验证码表
class EmailVerifyRecord(models.Model):
    # 发送选项
    SEND_CHOICE = (
        ("register", "注册"),
        ("forget", "找回密码"),
        ("update", u"修改邮箱")
    )
    # 验证码
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(choices=SEND_CHOICE, max_length=10, verbose_name="发送类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = "邮箱验证码列表"

    def __str__(self):
        return self.code


# 轮播图表
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(
        upload_to="banner/%Y/%m",
        verbose_name="轮播图",
        max_length=100,
    )
    url = models.URLField(max_length=100, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
