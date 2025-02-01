from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

def contact(subject, message):
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            {settings.EMAIL_RECIPIENT},
            fail_silently=False  
        )
        return True
    except Exception as e:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Error while sending mail : {e}")
        with open('errors.log', 'a') as f:
            f.write(f"[{current_time}]\nError message: {e}\n")

        return False
