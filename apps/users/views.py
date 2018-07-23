#encoding=utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django.contrib.auth.hashers import make_password

from forms import LoginForms, RegisterForm, ForgetForm, ModifyPwdForm
from utils.email_send import send_email
from .models import UserProfile,EmailVertifyRecord


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {"register_form": register_form})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get("email", "")
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {"register_form": register_form, "msg": u"邮箱已存在"})
                # return redirect('/register',{"register_form": register_form, "msg": u"邮箱已存在"})
            password = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.email = email
            user_profile.username = email
            user_profile.is_active = False
            user_profile.password = make_password(password)
            user_profile.save()

            send_email(email, "register")
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {"register_form": register_form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForms(request.POST)
        if login_form.is_valid():
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return render(request, 'login.html', {"msg": u"请用邮箱激活用户"})
            else:
                return render(request, 'login.html', {"msg": u"用户名或密码错误"})
        else:
            return render(request, 'login.html', {"login_form": login_form})


class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailVertifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                try:
                    user = UserProfile.objects.get(email=email)
                    user.is_active = True
                    user.save()
                except:
                    print "user is not exist!email is:%s" % email
        else:
            return render(request, 'active_fail.html')
        return redirect('/login/')


class ForgetView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {"forget_form": forget_form})
    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            send_status = send_email(email=email, send_type="forget")
            if send_status:
                return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {"forget_form": forget_form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVertifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {"email": email})
        else:
            return render(request, 'active_fail.html')


class ModifyView(View):
    def post(self, request):
        modify_pwd_form = ModifyPwdForm(request.POST)
        if modify_pwd_form.is_valid():
            email = request.POST.get("email", "")
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {"email": email, "msg": u"密码不一致"})
            else:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd1)
                user.save()
                return redirect('/login')
        else:
            email = request.POST.get("email", "")
            return render(request, 'password_reset.html', {"email": email, "modify_pwd_form": modify_pwd_form})

