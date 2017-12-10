from django import forms

from articles.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article', 'add_time')
