from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.dispatch import receiver

from .models import UserProfile


@receiver(user_logged_in)
def successful_login(sender, request, user, **kwargs):
    user.successful_logins += 1
    user.save()


@receiver(user_login_failed)
def failed_login(sender, credentials, **kwargs):
    user = UserProfile.objects.get(username=credentials.get("username"))
    user.failed_logins += 1
    user.save()
