from django.shortcuts import render
from django.contrib.auth import authenticate,login

def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
