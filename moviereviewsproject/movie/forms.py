from django.forms import ModelForm, Textarea, NumberInput
from .models import Review

class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['rating'].widget.attrs.update({'class': 'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})
    class Meta:
        model = Review
        fields = ['text', 'rating', 'watchAgain']
        # labels = {'rating':('Rating 0 to 10'), 'watchAgain': ('Watch Again')}
        widgets = {'text': Textarea(attrs={'rows':4}), 'rating': NumberInput()}
        # fields = ['text', 'watchAgain']
        labels = {'watchAgain': ('Watch Again')}
        # widgets = {'text': Textarea(attrs={'rows':4})}