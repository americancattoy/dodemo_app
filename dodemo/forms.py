from django import forms
from.models import DodemoModel
from django.contrib.auth.models import User

class PostForm(forms.Form):
    content = forms.CharField(max_length=140, \
        widget=forms.Textarea(attrs={'class':'form-control', 'rows':2}))

def __int__(self, user, *args, **kwargs)
