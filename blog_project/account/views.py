from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) #아이디와 비번을 입력하고 로그인 버튼을 눌렀을때
        if form.is_valid():
            auth_login(request, form.get_user()) #로그인 코드
        return redirect('index')
    else: #login 페이지 처음 들어갔을때
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('index')