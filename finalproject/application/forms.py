from django import forms

class FormAfterLogin(forms.Form):
    url_photo = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"placeholder": "Ingresa url de la imagen"}))
    title = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={"placeholder": "Título"}))
    description = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"placeholder": "Descripción"}))
    tags = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"placeholder": "Ejemplo: HTML, CSS, JS, etc..."}))
    url_github = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"placeholder": "Ejemplo: https://github.com/..."}))

 