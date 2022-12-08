from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

""" 
username
email 
password1
password2 
En el formulario tener una sección para confirmar que ambos passwords sean iguales

Si queremos aumentar más campos al registro podemos hacer un CustomForm y heredar de UserCreationForm
"""

class CreateUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def save(self, commit=True):
        user = super(CreateUser, self).save(commit=False)

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user    