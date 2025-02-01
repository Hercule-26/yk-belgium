from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .contact import contact
class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context    

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            subject = f"Formulaire de contact"
            message_content = f"Email: {email} \n\nMessage: {message}"

            email_sent = contact(subject, message_content)
            if email_sent:
                messages.success(request, _("Your message has been sent successfully!"))
            else:
                messages.warning(request, _("An error occurred while sending your message. Please try again later."))
    else:
        form = ContactForm()
        
    return redirect(request.META.get('HTTP_REFERER', 'contact'))