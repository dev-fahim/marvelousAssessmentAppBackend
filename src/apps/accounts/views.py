from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import reverse
from django.contrib import messages

# Create your views here.


def login_view(request, template_name="login.html"):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponsePermanentRedirect(reverse('home:index'))
            messages.warning(request, 'Your are not an active user.')
            return render(request, template_name, {'username': username, 'password': password})
        messages.error(request, 'Invalid username or password.')
        return render(request, template_name, {'username': username, 'password': password})
    return render(request, template_name, {'username': '', 'password': ''})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponsePermanentRedirect(reverse("auth:login_view"))
