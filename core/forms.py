from django import forms

from core.models import Comment, Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'cols': 15}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['email', 'message']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'cols': 15})
        }
