from .models import Review, Cottage
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


class ReviewForm(forms.ModelForm):
    cottage = forms.ModelChoiceField(
        queryset=Cottage.objects.all(),
        empty_label="Select Cottage",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Review
        fields = ['title', 'body', 'rating', 'featured_image', 'cottage']
