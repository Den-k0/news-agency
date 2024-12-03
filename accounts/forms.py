from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Redactor


class RedactorCreationForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = ('username', 'first_name', 'last_name', 'email', 'years_of_experience')


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ('first_name', 'last_name', 'email', 'years_of_experience')

