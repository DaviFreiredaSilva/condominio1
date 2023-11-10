from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login

def loginUser(request):
    context = {
        'pagename': 'login',
    }

    return render(request, 'accounts/login.html', context)

def authLogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
        else:
            return redirect('authError')
        return redirect(request.session['last_page_before_login'])

def authLogout(request):
    logout(request)
    return redirect('index')

def authError(request):

    return render(request, 'accounts/auth-error.html')