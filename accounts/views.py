from django.shortcuts import render

from django.views import generic
import logging
from django.contrib import messages


from django.utils.crypto import get_random_string
from .models import CustomUser, Team
from .forms import TeamCreateForm, TeamJoinForm
from django.urls import reverse_lazy

# scheduleから
import sys
sys.path.append('../')
from schedule import mixins
import datetime


logger = logging.getLogger(__name__)

# Create your views here.

class TeamCreateView(mixins.MonthCalendarMixin, generic.CreateView):
	model = Team
	template_name = "team_create.html"
	form_class = TeamCreateForm
	success_url = reverse_lazy("schedule:index")

	#日にちを持つのに必要
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		calendar_context = self.get_month_calendar()
		context.update(calendar_context)
		return context

	def form_valid(self, form):
		team = form.save(commit=False)
		team.code = get_random_string(30)
		team.save()
		team.members.add(self.request.user)
		
		myuser = self.request.user
		myuser.is_team_admin = True
		myuser.is_team_member = True
		myuser.save()
		messages.success(self.request, "OK")
		return super().form_valid(form)

	def form_invalid(self, form):
		messages.error(self.request, "失敗")
		return super().form_invalid(form)

class TeamJoinView(mixins.MonthCalendarMixin, generic.CreateView):
	model = Team
	template_name = "team_join.html"
	form_class = TeamJoinForm
	success_url = reverse_lazy("accounts:team_list")

	#日にちを持つのに必要
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		calendar_context = self.get_month_calendar()
		context.update(calendar_context)
		return context

	def form_valid(self, form):
		code = form.cleaned_data['code']
		team = Team.objects.get(code=code)
		team.members.add(self.request.user)

		myuser = self.request.user
		myuser.is_team_member = True
		myuser.save()

		messages.success(self.request, "OK")
		return super().form_valid(form)
