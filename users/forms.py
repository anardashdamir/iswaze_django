from dataclasses import field
import email
from pyexpat import model
from tkinter import S
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message, Profile, Skill

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

        labels = {
            'first_name': 'Ad',
            'email': 'E-mail',
            'username': 'İstifadəçi adı',
            'password1': 'Şifrə',
            'password2': "Şifrəni təstiqləyin"
        }


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input '})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username',
         'location', 'short_intro', 'profile_image',
         'social_github', 'social_linkedin', 'social_twitter', 'social_website', 'social_youtube']

        labels = {
            'name': 'Ad',
            'email': 'E-mail',
            'username': 'İstifadəçi adı',
            'short_intro': 'Bio',
            'location': 'Məkan',
            'short_intro': 'Qısa başlıq',
            'profile_image':'Profil Fotosu',
            'social_github': 'github',
            'social_linedin': 'linkedin',
            'social_twitter': 'twitter',
            'social_website': 'website',
            'social_youtube': 'youtube'
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)


        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input '})

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner'] #Bu xaric her hey
        labels = {
            'name': 'Başlıq',
            'description': 'Detallı'
        }


    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input '})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']
        
        labels = {
            'name': 'Ad',
            'subject': 'Mövzu başlığı',
            'body': 'Mətn',
        }


    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})