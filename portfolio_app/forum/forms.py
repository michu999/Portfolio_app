from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'bg-gray-700 text-white rounded-md p-3 w-full',
                'rows': 3,
                'placeholder': 'Write a comment...'
            }),
        }