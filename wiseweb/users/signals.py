from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver
from django.shortcuts import redirect
from django.urls import reverse

from .models import UserProfile


@receiver(user_logged_in)
def successful_login(sender, request, user, **kwargs):
    user.successful_logins += 1
    user.save()


@receiver(user_login_failed)
def failed_login(sender, credentials, **kwargs):
    if UserProfile.objects.filter(username=credentials.get("username")).exists():
        user = UserProfile.objects.get(username=credentials.get("username"))
        user.failed_logins += 1
        user.save()
    else:
        return redirect(reverse("login"))
