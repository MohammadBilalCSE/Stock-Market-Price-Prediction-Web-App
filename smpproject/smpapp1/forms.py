# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post  # Import the Profile model for the ProfileForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'photo']
        
    def clean_text(self):
        text = self.cleaned_data.get('text')
        words = text.split()
        if len(words) > 600:
            raise forms.ValidationError("The text must be 600 words or less.")
        return text
        