from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Reading

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ReadingSchedule(forms.ModelForm):
    class Meta:
        model = Reading
        fields = ['reader','date_reading','publication','title']