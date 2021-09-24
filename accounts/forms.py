from django import forms
from .models import Team


class TeamCreateForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ("name",)
		widgets = {'name': forms.TextInput(attrs={
	            'class': 'form-control',})}

class TeamJoinForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ("code",)
		widgets = {'code': forms.TextInput(attrs={
	            'class': 'form-control',})}
	    