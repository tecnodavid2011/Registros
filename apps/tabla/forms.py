from django import forms
from django.db import models
from django.contrib.auth.models import User
from  .models import tablaregistros, tablaaulas

class formulario(forms.ModelForm):
    class Meta:
        model = tablaregistros
        fields = [
            'nombre',  
            'apellido',
            ]

class formaula(forms.ModelForm):
    class Meta:
        model = tablaaulas
        fields = [ 
            'nombre',  
            'aula',
             ]