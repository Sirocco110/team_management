from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User,Group


# Create your models here.
class CustomUser(AbstractUser):
	is_team_admin = models.BooleanField(default=False, verbose_name='team_admin status')
	is_team_member = models.BooleanField(default=False, verbose_name='team_member status')

	class Meta:
		verbose_name_plural = 'CustomUser'

		
class Team(models.Model):
	name = models.CharField(max_length=128)
	members = models.ManyToManyField(CustomUser, blank=True)
	code = models.CharField(max_length=30, null=True)

	class Meta :
		verbose_name_plural = "Team"

	def __str__(self):
		return self.name

