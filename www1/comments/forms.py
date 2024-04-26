from django import forms
from .models import Comment
from django.utils import timezone


class CreateForm(forms.Form):
    text = forms.CharField(max_length=500, label="Comment text")
    author = forms.CharField(max_length=100, label="Author")
    published_from = forms.DateField()
        
    def create_comment(self):
        data = self.cleaned_data
        Comment(text = data["text"], author = data["author"], 
                creation_date = timezone.now(), published_from = data["published_from"]).save()
