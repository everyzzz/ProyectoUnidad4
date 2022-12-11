from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from application.models import FormData
from application.forms import FormAfterLogin


class Index(TemplateView):
    extra_context = {"form": FormData.objects.all()}
    template_name = "index.html"

    def get_context_data(self):
        context= {}
        context["form"] = FormData.objects.all()
        return context


class Form(LoginRequiredMixin, FormView):
    model = FormData
    template_name = "form.html"
    form_class = FormAfterLogin

    def form_valid(self, form):
        FormData.objects.create(**form.cleaned_data)
        return redirect("index")