from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.urls import reverse

from .forms import UserProfileForm
from .models import UserProfile


def login(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request=request,
                                     username=username,
                                     password=password)
            if user and user.is_active:
                auth.login(request=request,
                           user=user)
                return redirect(reverse('users:profile'))
        else:
            messages.error(request, "Неверное имя пользователя или пароль")
            return redirect(reverse("login"))

    else:
        form = UserProfileForm()
    context = {'form': form}
    return render(request=request,
                  template_name='users/login.html',
                  context=context)


def profile(request):
    user = request.user if isinstance(request.user, AnonymousUser) \
        else UserProfile.objects.get(username=request.user.username)

    successful_logins = user.successful_logins if not user.is_anonymous else 0
    failed_logins = user.failed_logins if not user.is_anonymous else 0

    total_logins = successful_logins + failed_logins
    success_percentage = (successful_logins / total_logins) * 100 if total_logins > 0 else 0
    failed_percentage = (failed_logins / total_logins) * 100 if total_logins > 0 else 0

    if successful_logins > failed_logins:
        style_class = "success-style"
    elif successful_logins < failed_logins:
        style_class = "failure-style"
    else:
        style_class = ""

    context = {
        'user': user,
        'successful_logins': successful_logins,
        'failed_logins': failed_logins,
        'success_percentage': success_percentage,
        'style_class': style_class,
        'failed_percentage': failed_percentage,
    }

    return render(request=request,
                  template_name='users/profile.html',
                  context=context)
