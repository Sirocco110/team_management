from django.shortcuts import render
from django.views import generic

from .forms import InquiryForm

import logging
from django.urls import reverse_lazy
from django.contrib import messages

#schedule用
from . import mixins
from .models import Schedule
from django.shortcuts import redirect
from .forms import RegisterForm
import datetime

from accounts.models import Team

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(mixins.MonthCalendarMixin, generic.TemplateView):
    template_name = "index.html"

    #日にちを持つのに必要
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)

        # myuser = self.request.user
        # teams = myuser.team_set.all()
        # team = teams[0]
        # context["team"] = team
        
        return context

class InquiryView(mixins.MonthCalendarMixin, generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('schedule:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

    #日にちを持つのに必要
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context

class MonthWithScheduleCalendar(mixins.MonthWithScheduleMixin, generic.TemplateView):
    """スケジュール付きの月間カレンダーを表示するビュー"""
    template_name = 'month_with_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        myuser = self.request.user
        context["myteam"] = Team.objects.get(members=myuser)
        return context

# TR登録
class RegisterView(mixins.MonthCalendarMixin, generic.CreateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'register.html'
    model = Schedule
    date_field = 'date'
    form_class = RegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        month_calendar_context = self.get_month_calendar()
        context.update(month_calendar_context)
        return context

    def form_valid(self, form):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        schedule = form.save(commit=False)
        schedule.date = date

        myuser = self.request.user
        schedule.team = Team.objects.get(members=myuser)

        schedule.save()
        return redirect('schedule:month_with_schedule', year=date.year, month=date.month)


# TR詳細
class ScheduleDetailView(mixins.MonthCalendarMixin, generic.DetailView):
    template_name = 'schedule_detail.html'
    model = Schedule
    date_field = 'date'

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
        return context

# TR編集
class ScheduleUpdateView(mixins.MonthCalendarMixin, generic.UpdateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'schedule_update.html'
    model = Schedule
    date_field = 'date'
    form_class = RegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        # context.update(week_calendar_context)
        context.update(month_calendar_context)
        return context

    def get_success_url(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        pk = self.kwargs.get('pk')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        return reverse_lazy("schedule:schedule_detail", kwargs={"year": year, "month": month, "day":day, "pk": pk})

    def form_valid(self, form):
        return super().form_valid(form)

# TR削除
class ScheduleDeleteView(mixins.MonthCalendarMixin, generic.DeleteView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'schedule_delete.html'
    model = Schedule
    date_field = 'date'
    # form_class = RegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        # context.update(week_calendar_context)
        context.update(month_calendar_context)
        return context

    def get_success_url(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        pk = self.kwargs.get('pk')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        return reverse_lazy("schedule:month_with_schedule", kwargs={"year": year, "month": month})

    def form_valid(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class UserInfoView(mixins.MonthCalendarMixin, generic.ListView):
    model = Team
    template_name = "user_info.html"

    #日にちを持つのに必要
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)

        myuser = self.request.user
        teams = myuser.team_set.all()

        context["teams"] = teams

        return context
