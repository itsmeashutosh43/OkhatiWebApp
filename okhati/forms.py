from django import forms
from django.contrib.auth.forms import UserCreationForm

class MedForm(forms.Form):
	medName=forms.CharField(help_text="Enter medicine name")
	forDisease=forms.CharField(help_text="Enter the disease or illness")
	price=forms.CharField(help_text="Enter the price")


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	