from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import Contact

class HomeView(TemplateView):
    template_name = 'page/home.html'


class AboutView(TemplateView):
    template_name = 'page/about.html'


class ContactView(CreateView):
    template_name = 'page/contact.html'
    success_url = '/'
    model = Contact
    fields = ('firstname', 'lastname', 'phone', 'email', 'infromation')
