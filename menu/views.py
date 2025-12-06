from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Category, Manls
from .forms import CategoryForm,ManlsForm
from django.views.generic.edit import FormMixin
from reservation.forms import ProfileForm
from django.urls import reverse_lazy
from reservation.models import Profile
from core.models import Chefs

class MenuView(ListView, FormMixin):
    template_name = "menu/menu.html"
    queryset = Profile.objects.all()
    context_object_name = 'chefs'
    form_class = ProfileForm
    success_url = reverse_lazy('home')


    def get_queryset(self):
        profile = Profile.objects.all()
        return profile

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('home')
        else:
            form = ProfileForm()
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['chefs'] = Chefs.objects.all()[:4]
        context['form'] = self.get_form()
        context['google_map_url'] = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2922.3268090152345!2d65.7851253!3d38.845298!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3f4ea6219349c8fb%3A0x9879a3d21a724458!2sASI%20Park!5e0!3m2!1sen!2s!4v1720971023456!5m2!1sen!1s"
        return context

    def get_success_url(self):
        return reverse_lazy('home')

class ManlsView(ListView):
    form_class = ManlsForm
    template_name = 'menu/manls.html'
    queryset = Manls.objects.all()
    context_object_name = 'categories'


    
