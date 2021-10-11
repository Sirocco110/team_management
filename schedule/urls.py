from django.urls import path

from . import views

app_name = "schedule"
urlpatterns = [
	path("",views.IndexView.as_view(), name="index"),
	path("inquiry/", views.InquiryView.as_view(), name="inquiry"),
	path('month_with_schedule/', views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('month_with_schedule/<int:year>/<int:month>/', views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path("register_schedule/<int:year>_<int:month>_<int:day>/", views.RegisterView.as_view(), name="register"),
    path("schedule_detail/<int:year>_<int:month>_<int:day>/<int:pk>/", views.ScheduleDetailView.as_view(), name="schedule_detail"),
    path("schedule_update/<int:year>_<int:month>_<int:day>/<int:pk>/", views.ScheduleUpdateView.as_view(), name="schedule_update"),
    path("schedule_delete/<int:year>_<int:month>_<int:day>/<int:pk>/", views.ScheduleDeleteView.as_view(), name="schedule_delete"),
]