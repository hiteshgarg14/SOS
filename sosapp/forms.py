from django import forms
from .models import NonUserContactModel, ReportOnceModel, IExperienceModel
from tinymce.widgets import TinyMCE

class NonUserContactForm(forms.ModelForm):

    class Meta:
        model = NonUserContactModel
        fields = '__all__'


class ReportOnceForm(forms.ModelForm):

	class Meta:
		model = ReportOnceModel
		fields = ['r_details']

class IExperienceForm(forms.ModelForm):
	
	class Meta:
		model = IExperienceModel
		fields = ['i_details']		