from django import forms
from .models import CustomUser

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture', 'bio', 'linkedin_url', 'email']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }