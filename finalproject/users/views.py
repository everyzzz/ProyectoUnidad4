from django.shortcuts import render, redirect
from users.forms import CreateUser
from django.views.generic import CreateView

class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = CreateUser
    def form_valid(self, form):
        form.save()
        return redirect('login')