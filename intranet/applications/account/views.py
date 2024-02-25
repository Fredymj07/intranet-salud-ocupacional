from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (
    View
)
from django.views.generic.edit import (
    FormView
)
from .forms import (
    UserRegisterForm, 
    LoginForm,
    UpdatePasswordForm,
)
from .models import User


class LoginUser(FormView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home-user')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)
    

class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'account_app:user-login'
            )
        )
        
            
class UserRegisterView(FormView):
    template_name = 'account/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('account_app:user-login')

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['full_name'],
            form.cleaned_data['password1'],
            ocupation=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            date_birth=form.cleaned_data['date_birth'],
        )
        return super(UserRegisterView, self).form_valid(form)


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'account/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('account_app:user-login')
    login_url = reverse_lazy('account_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            email=usuario.email,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)