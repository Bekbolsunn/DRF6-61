from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email(email, code):
    print("SENDING...")
    send_mail(
        "Регистрация в shop_api",
        f"ваш код для подтверждения: {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    print("SENT.")
    return "OK"


@shared_task
def send_birthday_message():
    print("SENDING...")
    send_mail(
        "happy birthday!",
        "с вылуплением",
        settings.EMAIL_HOST_USER,
        ["тута_почта"],
        fail_silently=False,
    )
    print("SENT.")
    return "OK"
