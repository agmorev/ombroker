from email.message import EmailMessage
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class MainView(SuccessMessageMixin, FormView):
    template_name = 'main/main.html'
    form_class = ContactForm
    success_url = '/'
    success_message = _('Повідомлення успішно відправлено')
    
    def form_valid(self, form):
        form.send_email()       
        return super().form_valid(form)