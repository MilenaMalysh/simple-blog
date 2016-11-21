from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    '''class Meta:
        model = Post
        fields = ('title', 'text',)
        #widgets = {'text': CKEditorWidget()}'''
    class Meta:
        model = Post
        fields = ('title', 'text',)



class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
