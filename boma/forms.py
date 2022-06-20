from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import NeighbourHood, Profile, Post,Business
from django.forms import ModelForm, TextInput, EmailInput,ImageField, Textarea



class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)

class UpdateHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'

