from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description','weight','length', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 4}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight (kg)'}),
            'length': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Length (cm)'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        