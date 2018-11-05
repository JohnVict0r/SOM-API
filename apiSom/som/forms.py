from django import forms

from .models import Post

class SomForm(forms.ModelForm):

    class Meta:
        model = Som
        fields = ('red', 'green', 'blue',)