
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm

from .models import Contact
from .models import Image
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'content']




class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title','text','photo']


# class PasswordChangingForm(PasswordChangeForm):
#     class Meta:
#         model=User
#         fields=['old_password','new_password']
#
#

# class EditProfileForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']