from django.db import models

#カレンダー用
import datetime
from django.utils import timezone
from accounts.models import CustomUser, Team

# Create your models here.

class Schedule(models.Model):
	"""docstring for Schedule"""
	team = models.ForeignKey(Team, verbose_name="チーム", null=True, on_delete=models.PROTECT)
	summary = models.CharField('概要', max_length=50)
	place = models.CharField("場所", max_length=50, null=True)
	start_time = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
	end_time = models.TimeField('終了時間', default=datetime.time(7, 0, 0))
	description = models.TextField('詳細な説明', blank=True)
	date = models.DateField('日付')
	created_at = models.DateTimeField('作成日', default=timezone.now)

	def __str__(self):
		return self.summary