from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_tag', 'author', 'body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'This is title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control', 'placeholder':'This is title_tag'}),
            'author':forms.Select(attrs={'class':'form-control', 'placeholder':'This is author'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'This is body'}),
        }