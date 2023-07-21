from django.core.mail import EmailMessage
from django.http import HttpResponse


def emailSend(*args):
    email = EmailMessage(subject=args[0], body=args[1], to=[args[2]])
    email.send()
    return HttpResponse(status=204)
