from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields=('comment','author', 'post')


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):

        model = CustomUser
        fields = UserCreationForm.Meta.fields = ("username",'age','image')

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = "__all__"
