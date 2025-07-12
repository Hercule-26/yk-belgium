from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
import logging
from .contact import send_email

class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context    

logger = logging.getLogger(__name__)

def send_form(request):
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = "Message depuis le formulaire de contact"
            message_content = f"Email: {email} \n\nMessage: \n{message}"
            email_sent = send_email(subject, message_content)
            if email_sent:
                messages.success(request, _("Your message has been sent successfully!"))
                return redirect('home:send-form')  # ou une autre URL
            else:
                logger.error("Failed to send email. Check logs file for more details")
                with open('errors.log', 'a') as f:
                    f.write(f"Failed to send email.\nEmail Recipient: {email}\nMessage Content: {message}\n\n")
                messages.warning(request, _("An error occurred while sending your message. Please try again later."))
        else:
            messages.error(request, _("There was an issue with your form. Please check your input."))
    return render(request, 'home/home.html', {'form': form})