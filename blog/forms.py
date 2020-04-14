from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    """Form to let users share posts by email."""

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """Build a form dynamically from the Comment Model."""

    class Meta:
        """Indicate shich model to use to build the form."""

        model = Comment
        fields = ('name', 'email', 'body')  # List of fields to include in form


class SearchForm(forms.Form):
    # Use the query field to let the users introduce search terms.
    query = forms.CharField()
