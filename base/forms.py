from django import forms
from .models import Document

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='',
        # help_text="Формат xmls"
    )
    
    class Meta:
        model = Document