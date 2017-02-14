from django import forms
from .models import NonUserContactModel, ReportOnceModel, IExperienceModel, ProfileModel
from tinymce.widgets import TinyMCE
from django.contrib.auth.models import User
from django.conf import settings

class NonUserContactForm(forms.ModelForm):
    class Meta:
        model = NonUserContactModel
        fields = '__all__'


class ReportOnceForm(forms.ModelForm):
	class Meta:
		model = ReportOnceModel
		fields = ['title', 'details']

class IExperienceForm(forms.ModelForm):
	class Meta:
		model = IExperienceModel
		fields = ['title', 'details']


# Edit Profile Forms (5)
class ProfileOverviewForm(forms.ModelForm):
	# birthdate = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

	class Meta:
		model = ProfileModel
		fields = ['gender','birthdate']

class UserOverviewForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name','last_name']

class ProfileContactForm(forms.ModelForm):
	class Meta:
		model = ProfileModel
		fields = ['mobile','address']

class UserContactForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email']

class ProfileProfessionalForm(forms.ModelForm):
	class Meta:
		model = ProfileModel
		fields = ['p_title','p_company','p_city','p_time_from','p_time_to']
