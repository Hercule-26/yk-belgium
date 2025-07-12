import re
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

    def clean_message(self):
        message = self.cleaned_data['message']
        
        # Detection of dangerious patterns (script, command injection, ...)
        forbidden_patterns = [
        r'<script.*?>.*?</script>',                       
        r'(?i)(onerror|onload|onclick)\s*=',              
        r'(?i)javascript:',                               
        r'(?i)\b(curl|wget|nslookup|ping|bash|sh)\b',     
        r'[`$&|><]',                                      
        r'(?i)document\.cookie',
    ]
        
        for pattern in forbidden_patterns:
            if re.search(pattern, message, re.IGNORECASE):
                raise forms.ValidationError(_("Your message contains forbidden content."))
        
        return message
