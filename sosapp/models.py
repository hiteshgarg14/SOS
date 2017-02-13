from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class NonUserContactModel(models.Model):
    name = models.CharField(max_length=120, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex],max_length=15 ,blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name


class ReportOnceModel(models.Model):
	r_user = models.ForeignKey(User)
	title = models.CharField(max_length=250,blank=False)
	details = HTMLField()
	r_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-r_created',)

	def __str__(self):
		return self.r_title

class IExperienceModel(models.Model):
	i_user = models.ForeignKey(User)
	title = models.CharField(max_length=250,blank=False)
	details = HTMLField()
	i_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-i_created',)

	def __str__(self):
		return self.i_title

class ProfileModel(models.Model):
	GENDER_CHOICES = (
		('female','Female'),
		('male','Male'),
	)
	user = models.OneToOneField(User)
	gender = models.CharField(max_length=25, blank=True, choices=GENDER_CHOICES, default='male')
	birthdate = models.DateField(blank=True, null=True)
	mobile = models.CharField(max_length=12, blank=True)
	address = models.CharField(max_length=500, blank=True)
	p_title = models.CharField(max_length=150, blank=True)
	p_company = models.CharField(max_length=150, blank=True)
	p_city = models.CharField(max_length=150, blank=True)
	p_time_from = models.DateField(blank=True, null=True)
	p_time_to = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.user.username
