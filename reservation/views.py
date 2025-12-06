from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView,CreateView,UpdateView,DeleteView
from .models import Profile
from .forms import ProfileForm
from menu.models import Category
from core.models import Chefs
from django.shortcuts import redirect
from django.views.generic.edit import FormMixin


class ProfileView(FormMixin,ListView):
    model = Profile
    template_name = 'reservation/reservation_home.html'
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    
    def get_queryset(self):
        reservation = Profile.objects.all()
        return reservation

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
    

class ProfileListView(ListView):
    model = Profile
    template_name = 'reservation/reservation_list.html'
    success_url = reverse_lazy('home')
    context_object_name = 'profiles'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profile.objects.all()
        return context
