from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import FormView, UpdateView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, get_user_model


user = get_user_model()

class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'user/register.html'    
    success_url = '/signedup'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'    
    success_url = '/loggedin'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)

class ProfileView(UpdateView):
    model = user
    fields = (
        'username',
        'avatar',
        'bio',
        'website'
    )
    template_name = 'user/profile_update.html'
    success_url = '/'



    def get_object(self, queryset=None):
        return self.request.user

def signup(request):
    return HttpResponse("you successfully signed up.")   

def loggedin(request):
    return HttpResponse("you successfully logged in.")   
