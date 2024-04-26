# forms.py
from django import forms
from .models import student,company,job,studymaterial

class StudentForm(forms.ModelForm):
    class Meta:
        model = student  # Updated to match the renamed model class
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = '__all__'


class JobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'


class MaterialForm(forms.ModelForm):
    class Meta:
        model = studymaterial
        fields = '__all__'
        

class UserModelForm(forms.ModelForm):
	ORG_SIZE_CHOICES = (
		('Small', 'Small'),
		('Medium', 'Medium'),
		('Large', 'Large')
	)
	username         = forms.TextInput(attrs={'class': 'form-control ','required':True})
	last_name		 = forms.TextInput(attrs={'class': 'form-control ','required':True})
	password         = forms.CharField(label='Password', widget=forms.PasswordInput)
	confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)



