from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Contact
from .forms import ContactForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin

# from django.views.generic.edit import FormMixin

# class ContactView(ListView):
#     template_name = 'contact/create_contact.html'
#     queryset = Contact.objects.all()
#     context_object_name = 'create_contact'
#     context_object_name = 'contact_info'
    

class ContactView(CreateView, ListView, FormMixin):
    template_name = 'contact/create_contact.html'
    queryset = Contact.objects.all()
    success_url = reverse_lazy('create_contact')
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = Contact.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



