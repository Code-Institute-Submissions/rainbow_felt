from django import forms
from .models import Custom


# Custom product request form
class CustomProductForm(forms.ModelForm):

	custom_description = forms.CharField(widget=forms.Textarea)
	email = forms.EmailField()

	class Meta:
		model = Custom
		fields = ['custom_description', 'email']
		