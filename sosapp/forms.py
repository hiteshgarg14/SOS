from django import forms
from .models import NonUserContactModel

class NonUserContactForm(forms.ModelForm):

    class Meta:
        model = NonUserContactModel
        fields = '__all__'
