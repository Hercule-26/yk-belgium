from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactFormFR, ContactFormNL
from django.contrib import messages

from .contact import contact
class HomeViewFR(TemplateView):
    template_name = "home/home-fr.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactFormFR()
        return context    
    
class HomeViewNL(TemplateView):
    template_name = "home/home-nl.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactFormNL()
        return context    

def contact_view(request):
    if request.method == 'POST':
        form = ContactFormFR(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            subject = f"Formulaire de contact"
            message_content = f"Email: {email} \n\nMessage: {message}"

            email_sent = contact(subject, message_content)
            referer = request.META.get('HTTP_REFERER', '')  # URL de la page précédente
            if email_sent:
                if referer == 'be-fr/':
                    messages.success(request, "Votre message a été envoyé avec succès !")
                else:
                    messages.success(request, "Je bericht is succesvol verzonden!")
            else:
                if referer == 'be-fr/':
                    messages.warning(request, "Une erreur est survenue lors de l'envoi de votre message. Veuillez réessayer plus tard.")
                else:
                    messages.warning(request, "Er is een fout opgetreden tijdens het verzenden van je bericht. Probeer het later nog eens.")
    else:
        form = ContactFormFR()
        
    return redirect(request.META.get('HTTP_REFERER', 'contact'))