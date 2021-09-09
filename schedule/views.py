from django.shortcuts import render
from django.views import generic

from .forms import InquiryForm

import logging
from django.urls import reverse_lazy
from django.contrib import messages

#schedule用
from . import mixins

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(mixins.MonthCalendarMixin, generic.TemplateView):
    template_name = "index.html"

    #日にちを持つのに必要
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
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

class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'schedule.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context