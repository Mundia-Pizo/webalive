from django import forms

class ContactForm(forms.ModelForm):
    email = forms.EmailField()
    message = forms.TimeField()