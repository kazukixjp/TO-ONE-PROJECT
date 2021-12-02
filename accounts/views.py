from django.shortcuts import render, redirect
from allauth.account import views


class LoginView(views.LoginView):
    #template_name = 'accounts/login.html'
    template_name = 'accounts/login-glass.html'


class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'
    #template_name = 'accounts/logout-glass.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')


class SignupViews(views.SignupView):
    #template_name = 'accounts/signup.html'
    template_name = 'accounts/signup-glass.html'
