#encoding=utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.generic import View

from forms import LoginForms, RegisterForm


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        pass


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
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {"msg": u"用户名或密码错误"})
        else:
            return render(request, 'login.html', {"login_form": login_form})
