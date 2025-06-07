from .models import Review
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'body', 'featured_image')
        widgets = {
            'title': forms.Textarea(attrs={
                'placeholder': 'Write your title here...',
                'rows': 1,
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'Write your review here...',
                'rows': 10,
                'class': 'form-control'
            })
        }
