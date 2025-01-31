from django import forms

class ContactFormFR(forms.Form):
    email = forms.EmailField(
        label="Votre email",
        max_length=255,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'})
    )
    
    message = forms.CharField(
        label="Votre message",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Écrivez votre message ici...', 'rows': 5})
    )

class ContactFormNL(forms.Form):
    email = forms.EmailField(
        label="Uw e-mail",
        max_length=255,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Uw e-mail'})
    )
    
    message = forms.CharField(
        label="Uw bericht",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Schrijf hier uw bericht...', 'rows': 5})
    )
