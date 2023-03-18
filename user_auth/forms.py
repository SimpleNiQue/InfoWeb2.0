from typing import Any

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

nice_style = 'w-full px-4 py-2 mt-2 border rounded-md focus:outline-none focus:ring-1 focus:ring-blue-600'

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
            'class': nice_style,
            'placeholder': 'Email',
            }
        ),
        label='Username',
        label_suffix=''
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'type': 'password'
            }
        )
    )


class RegistrationForm(UserCreationForm):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {
            'class': nice_style,
            'placeholder': 'First Name'
        }
        self.fields['last_name'].widget.attrs = {
            'class': nice_style,
            'placeholder': 'Last Name'
        }
        self.fields['email'].widget.attrs = {
            'class': nice_style,
            'placeholder': 'Email'
        }

        self.fields['password1'].widget.attrs = {
            'class': nice_style,
            'placeholder': 'Enter a secure password'
        }

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
           user.save()
        return user