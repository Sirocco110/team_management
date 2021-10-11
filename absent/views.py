from django.shortcuts import render
from django.views import generic

import logging
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Absent, PreReview, Review

from schedule import mixins
from schedule.models import Schedule
from accounts.models import Team

from django.shortcuts import redirect
import datetime

from .forms import AbsentForm, PreReviewForm, ReviewForm

# Create your views here.

logger = logging.getLogger(__name__)


class AbsentView(mixins.MonthWithScheduleMixin, generic.ListView):
	template_name = 'absent.html'
	model = Schedule
	date_field = 'date'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		calendar_context = self.get_month_calendar()
		context.update(calendar_context)
		myuser = self.request.user
		context["myteam"] = Team.objects.get(members=myuser)
		return context

class AbsentRegisterView(mixins.MonthCalendarMixin, generic.DetailView):
	template_name = 'absent_register.html'
	model = Schedule
	date_field = 'date'
	# form_class = AbsentForm

	def get_days(self):
		month = self.kwargs.get('month')
		year = self.kwargs.get('year')
		day = self.kwargs.get('day')
		date = datetime.date(year=int(year), month=int(month), day=int(day))
		return date

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		month_calendar_context = self.get_month_calendar()
		context.update(month_calendar_context)
		context["form"] = AbsentForm
		return context

	def post(self, request, *args, **kwargs):
		month = self.kwargs.get('month')
		year = self.kwargs.get('year')
		day = self.kwargs.get('day')
		date = datetime.date(year=int(year), month=int(month), day=int(day))

		ab_form = AbsentForm(request.POST)
		ab_schedule = Schedule.objects.get(pk=self.kwargs['pk'])
		# 質問文変更ボタンがPOSTにあるとき
		if request.method == "POST":
			absent = ab_form.save(commit=False)
			absent.user = self.request.user
			absent.schedule = ab_schedule
			absent.save()
			return redirect('schedule:month_with_schedule', year=date.year, month=date.month)

		else:
			return redirect('schedule:index')


class ReviewView(mixins.MonthWithScheduleMixin, generic.ListView):
	template_name = 'review.html'
	model = Schedule
	date_field = 'date'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		calendar_context = self.get_month_calendar()
		context.update(calendar_context)
		myuser = self.request.user
		context["myteam"] = Team.objects.get(members=myuser)
		return context

class PreReviewRegisterView(mixins.MonthCalendarMixin, generic.DetailView):
	template_name = 'prereview_register.html'
	model = Schedule
	date_field = 'date'
	# form_class = AbsentForm

	def get_days(self):
		month = self.kwargs.get('month')
		year = self.kwargs.get('year')
		day = self.kwargs.get('day')
		date = datetime.date(year=int(year), month=int(month), day=int(day))
		return date

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		month_calendar_context = self.get_month_calendar()
		context.update(month_calendar_context)
		context["form"] = PreReviewForm
		return context

	def post(self, request, *args, **kwargs):
		month = self.kwargs.get('month')
		year = self.kwargs.get('year')
		day = self.kwargs.get('day')
		date = datetime.date(year=int(year), month=int(month), day=int(day))

		ab_form = PreReviewForm(request.POST)
		ab_schedule = Schedule.objects.get(pk=self.kwargs['pk'])
		# 質問文変更ボタンがPOSTにあるとき
		if request.method == "POST":
			prereview = ab_form.save(commit=False)
			prereview.user = self.request.user
			prereview.schedule = ab_schedule
			prereview.save()
			return redirect('schedule:month_with_schedule', year=date.year, month=date.month)

		else:
			return redirect('schedule:index')


class ReviewRegisterView(mixins.MonthCalendarMixin, generic.DetailView):
	template_name = 'review_register.html'
	model = Schedule
	date_field = 'date'
	# form_class = AbsentForm

	def get_days(self):
		month = self.kwargs.get('month')
		year = self.kwargs.get('year')
		day = self.kwargs.get('day')
		date = datetime.date(year=int(year), month=int(month), day=int(day))
		return date

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		month_calendar_context = self.get_month_calendar()
		context.update(month_calendar_context)
		context["form"] = ReviewForm

		review_schedule = Schedule.objects.get(pk=self.kwargs['pk'])
		user = self.request.user


		goal = PreReview.objects.filter(schedule=review_schedule,user=user)
		if goal.first() is None:
			context["goal"] = "設定されていません"
		else:
			goal = PreReview.objects.get(schedule=review_schedule,user=user)
			context["goal"] = goal.goal		

		return context

	def post(self, request, *args, **kwargs):
		month = self.kwargs.get('month')
		year = self.kwargs.get('year')
		day = self.kwargs.get('day')
		date = datetime.date(year=int(year), month=int(month), day=int(day))

		ab_form = ReviewForm(request.POST)
		ab_schedule = Schedule.objects.get(pk=self.kwargs['pk'])
		# 質問文変更ボタンがPOSTにあるとき
		if request.method == "POST":
			review = ab_form.save(commit=False)
			review.user = self.request.user
			review.schedule = ab_schedule
			review.save()
			return redirect('schedule:month_with_schedule', year=date.year, month=date.month)

		else:
			return redirect('schedule:index')

class AbsentCheckView(mixins.MonthCalendarMixin, generic.ListView):
	template_name = 'absent_check.html'
	model = Schedule
	date_field = 'date'
	# form_class = AbsentForm

	def get_days(self):
		month = self.kwargs.get('month')
		year = self.kwargs.get('year')
		day = self.kwargs.get('day')
		date = datetime.date(year=int(year), month=int(month), day=int(day))
		return date

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		month_calendar_context = self.get_month_calendar()
		context.update(month_calendar_context)

		myuser = self.request.user
		teams = myuser.team_set.all()
		schedule = Schedule.objects.get(pk=self.kwargs['pk'])
		context["Team"] = teams
		context["schedule"] = schedule
		absents = Absent.objects.filter(schedule=schedule)
		context["absents"] = absents
		return context

class ReviewCheckView(mixins.MonthCalendarMixin, generic.ListView):
	template_name = 'review_check.html'
	model = Schedule
	date_field = 'date'
	# form_class = AbsentForm

	def get_days(self):
		month = self.kwargs.get('month')
		year = self.kwargs.get('year')
		day = self.kwargs.get('day')
		date = datetime.date(year=int(year), month=int(month), day=int(day))
		return date

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		month_calendar_context = self.get_month_calendar()
		context.update(month_calendar_context)

		myuser = self.request.user
		teams = myuser.team_set.all()
		members = teams[0].members.all()
		print(members)

		schedule = Schedule.objects.get(pk=self.kwargs['pk'])
		context["Team"] = teams
		context["schedule"] = schedule
		# context["members"] = members

		prereviews = PreReview.objects.filter(schedule=schedule)
		# context["prereviews"] = prereviews
		reviews = Review.objects.filter(schedule=schedule)
		# context["reviews"] = reviews
		print(prereviews.filter(user=myuser))
		review_set = []
		for i in members:
			prereview = prereviews.filter(user=i)
			review = reviews.filter(user=i)
			review_set.append([i,prereview,review])
		context["review_sets"] = review_set
		return context


# person1 = Person.objects.get(id=1)
# >>> person1.hobbys.all()
			
