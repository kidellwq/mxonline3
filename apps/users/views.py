from django.shortcuts import render, HttpResponseRedirect, reverse
# 使用django自带的auth认证模块进行密码检验
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ActiveForm, ForgetForm
from utils.email_send import send_register_eamil


# 激活用户
class ActiveUserView(View):
    def get(self, request, active_code):
        # 查询邮箱验证记录是否存在
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        active_form = ActiveForm(request.GET)

        if all_record:
            for record in all_record:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'msg': "您的激活链接无效", "active_form": active_form})


# 基于函数来实现的登陆控制
def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', "")
        pass_word = request.POST.get('password', "")
        # 成功返回user对象，失败返回null
        user = authenticate(username=user_name, password=pass_word)

        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html',  {"msg": "用户名或密码错误! "})
    elif request.method == 'GET':
        return render(request, 'login.html')


# 基于类来实现登陆控制
class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', "")
            pass_word = request.POST.get('password', "")
            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html',  {"msg": "用户名或密码错误! "})
        else:
            return render(request, 'login.html', {'login_form': login_form})


# 登出功能
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


# 自定义authenticate方法，实现用户名邮箱均可登录
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 注册功能
class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            pass_word = request.POST.get('password', '')

            # 实例化一个userProfile对象，将前台的值存入
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name

            # 默认激活状态为false,只有通过邮箱验证才更改为true
            user_profile.is_active = False

            user_profile.password = make_password(pass_word)
            user_profile.save()

            # 发送注册邮件
            send_register_eamil(user_name, 'register')

            # 注册成功后，跳转到登录页面
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


# 找回密码
class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm()
        if forget_form.is_valid():
            email = request.POST.get('email')
            send_register_eamil(email, 'forget')
            return render(request, 'login.html', {"msg": "重置密码邮件已发送,请注意查收"})
        else:
            return render(request, 'forgetpwd.html', {"forget_from": forget_form })
