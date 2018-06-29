"""mxonline3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
import xadmin
from mxonline3.settings import MEDIA_ROOT
from django.views.static import serve
from django.views.generic import TemplateView
from users.views import LoginView, LogoutView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, IndexView
from organization.views import OrgView


urlpatterns = [
    # 后台
    path('xadmin/', xadmin.site.urls),
    # 首页
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    # 登陆
    # path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    # 登出
    path('logout/', LogoutView.as_view(), name='logout'),
    # 注册
    path('register/', RegisterView.as_view(), name='register'),
    # 忘记密码
    path('forgetpwd/', ForgetPwdView.as_view(), name='forget_pwd'),
    # 验证码
    path('captcha/', include('captcha.urls')),
    # 激活用户的url，邮箱里的连接
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    # 重置密码的链接
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    # 修改密码的链接
    path('modify/', ModifyPwdView.as_view(), name='modify_pwd'),

    # 机构首页
    # path('org-list/', OrgView.as_view(), name='org_list'),
    path('org/', include('organization.urls', namespace='org')),
    # 图片处理的url
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),

    # 课程首页
    path('course/', include('courses.urls', namespace='course')),

    # 个人中心
    path('users/', include('users.urls', namespace='users')),
]
