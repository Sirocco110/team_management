from django import forms
from django.core.mail import EmailMessage
from .models import Absent, PreReview, Review


class AbsentForm(forms.ModelForm):
	class Meta:
	    model = Absent
	    fields = ('reason',)
	    widgets = {
	        'reason': forms.TextInput(attrs={
	            'class': 'form-control',
	        }),
	    }


class PreReviewForm(forms.ModelForm):
	class Meta:
	    model = PreReview
	    fields = ('goal',)
	    widgets = {
	        'goal': forms.TextInput(attrs={
	            'class': 'form-control',
	        }),
	    }


class ReviewForm(forms.ModelForm):
	class Meta:
	    model = Review
	    fields = ('review',)
	    widgets = {
	        'review': forms.TextInput(attrs={
	            'class': 'form-control',
	        }),
	    }