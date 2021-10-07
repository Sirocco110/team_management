from django.urls import path

from . import views

app_name = "absent"

urlpatterns = [
	path("absent/<int:year>/<int:month>/", views.AbsentView.as_view(), name="absent"),
	path("absent_register/<int:year>_<int:month>_<int:day>/<int:pk>/", views.AbsentRegisterView.as_view(), name="absent_register"),
	path("review/<int:year>/<int:month>/", views.ReviewView.as_view(), name="review"),
	path("prereview_register/<int:year>_<int:month>_<int:day>/<int:pk>/", views.PreReviewRegisterView.as_view(), name="prereview_register"),
	path("review_register/<int:year>_<int:month>_<int:day>/<int:pk>/", views.ReviewRegisterView.as_view(), name="review_register"),
	path("absent_check/<int:year>_<int:month>_<int:day>/<int:pk>/", views.AbsentCheckView.as_view(), name="absent_check"),
	path("review_check/<int:year>_<int:month>_<int:day>/<int:pk>/", views.ReviewCheckView.as_view(), name="review_check"),
]