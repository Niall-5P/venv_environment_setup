# collaboration/forms.py
from django import forms
from .models import CollaborationRequest


class CollaborationRequestForm(forms.ModelForm):
    class Meta:
        model  = CollaborationRequest
        fields = ['full_name', 'email', 'brand_name', 'website', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
