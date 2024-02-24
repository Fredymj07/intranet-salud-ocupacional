from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    """_summary_
       Clase para crear un formulario personalizado para el registro de usuarios
    """
    first_name = forms.CharField(required=True, label='Nombres')
    last_name = forms.CharField(required=True, label='Apellidos')
    email = forms.EmailField(required=True, label='Correo Electrónico')

    def clean_email(self):
        """_summary_
           Método para validar que el correo no exista en la base de datos
        """
        email_user = self.cleaned_data['email'].lower()
        user_data = User.objects.filter(email=email_user)
        if user_data.count():
            raise ValidationError('El email ingresado ya se encuentra registrado.')
        return email_user
    
    def clean_username(self):
        """_summary_
           Método para validar que el nombre de usuario no exista en la base de datos
        """
        username = self.cleaned_data['username']
        user_data = User.objects.filter(username=username)
        if user_data.count():
            raise ValidationError('El nombre de usuario ingresado ya se encuentra registrado.')
        return username
    
    def save(self, commit=True):
        """_summary_
           Método para guardar el usuario en la base de datos
        """
        user_data = User.objects.create_user(
            self.cleaned_data['username'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password1'],
        )
        return user_data