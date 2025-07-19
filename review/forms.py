# review/forms.py
from django import forms
from .models import ReviewModel

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['content']
