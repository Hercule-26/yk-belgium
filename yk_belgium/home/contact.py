from django.core.mail import send_mail
from django.conf import settings

def contact(subject, message):
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            settings.EMAIL_RECIPIENT,
            fail_silently=False  
        )
        return True
    except Exception as e:
        print(f"Error while sending mail : {e}")
        return False
