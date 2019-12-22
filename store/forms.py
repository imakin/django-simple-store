from django import forms
from store import models

class PostForm(forms.ModelForm):
	class Meta:
		model = models.Customer
		fields = ['phone_number', 'name','email']
	url = forms.CharField(disabled=True, required=False)

	def save(self, commit=True):
		instance = super(PostForm, self).save(commit=False)
		if commit:
			instance.save()
		return instance


