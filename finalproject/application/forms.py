from django import forms

class FormAfterLogin(forms.Form):
    url_photo = forms.CharField(max_length=100)
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
    tags = forms.CharField(max_length=100)
    url_github = forms.CharField(max_length=100)

 