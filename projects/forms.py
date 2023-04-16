from dataclasses import field, fields
from django.forms import ModelForm
from django import forms
from .models import Project, Review


class ProjectForm(ModelForm): 
    class Meta:
        model = Project
        fields = ['title', 'featured_image','uploaded_file' , 'description', 'demo_link', 'source_link', 'tags']
        labels = {
            'title': 'Başlıq',
            'featured_image': "Başlıq Fotosu",
            'uploaded_file': "Fayl (pdf, doc ...)",
            'description': "Açıqlama",
            'demo_link': "Demo linki",
            'source_link': "Mənbə linki",
            'tags': 'Təqlər'
            
            
            
        }

        widgets ={
            'tags': forms.CheckboxSelectMultiple(),

        }


    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input '})

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Səsiniz',
            'body' : 'Koment...'
        }
        
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})