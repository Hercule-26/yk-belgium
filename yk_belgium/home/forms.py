from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    email = forms.EmailField(
        label=_("Your mail"),
        max_length=255,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Your mail')})
    )
    
    message = forms.CharField(
        label=_("Your message"),
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Type your text here'), 'rows': 5})
    )
