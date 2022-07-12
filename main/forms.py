from django import forms
from django.core.mail import EmailMessage
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label=_("Ім'я"))
    email = forms.EmailField(max_length=200, label=_("Email"))
    subject = forms.CharField(max_length=200, label=_("Тема"))
    message = forms.CharField(widget=forms.Textarea, label=_("Повідомлення"))
    
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = 'Повідомлення від ' + name + ',\n' + self.cleaned_data['message']
        msg = EmailMessage(
                subject,
                message,
                email,
                ['office@ombroker.pp.ua', ],
            )
        msg.content_subtype = "html"
        msg.send()