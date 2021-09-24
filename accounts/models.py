from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User,Group


# Create your models here.
class CustomUser(AbstractUser):

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

# class TeamUser(models.Model):
# 	# チームユーザーモデル
# 	user = models.ForeignKey(CustomUser, verbose_name="ユーザー",on_delete=models.PROTECT)
# 	teams = models.ManyToManyField(Team, blank = True)

# 	class Meta :
# 		verbose_name_plural = "TeamUser"

# 	def __str__(self):
# 		return self.user.username


# class TeamCode(models.Model):
# 	name = models.ForeignKey(Team, verbose_name="ユーザー",on_delete=models.PROTECT)
# 	code = models.CharField(max_length=128)

# 	class Meta :
# 		verbose_name_plural = "TeamCode"

# 	def __str__(self):
# 		return self.code