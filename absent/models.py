from django.db import models

from schedule.models import Schedule
from accounts.models import CustomUser
from django import forms

# Create your models here.

class Absent(models.Model):

	schedule = models.ForeignKey(Schedule, verbose_name="予定", on_delete=models.PROTECT)
	user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.PROTECT)
	reason = models.TextField('欠席理由', blank=True)
	
	def __str__(self):
		template = '{0.user.username} {0.schedule.summary} {0.schedule.date}'
		return template.format(self)

class PreReview(models.Model):

	schedule = models.ForeignKey(Schedule, verbose_name="予定", on_delete=models.PROTECT)
	user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.PROTECT)
	goal = models.CharField('目標', max_length=50, blank=True)

	def __str__(self):
		template = '{0.user.username} {0.schedule.summary} {0.schedule.date}'
		return template.format(self)

class Review(models.Model):

	schedule = models.ForeignKey(Schedule, verbose_name="予定", on_delete=models.PROTECT)
	user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.PROTECT)
	# point = forms.fields.ChoiceField(
 #        choices = (
 #            ('1', '1'),
 #            ('2', '2'),
 #            ('3', '3'),
 #            ('4', '4'),
 #            ('5', '5')
 #        ),
 #        required=True,
 #        widget=forms.widgets.Select,
 #        blank=True
 #    )
	review = models.TextField('振り返り', blank=True)

	def __str__(self):
		template = '{0.user.username} {0.schedule.summary} {0.schedule.date}'
		return template.format(self)