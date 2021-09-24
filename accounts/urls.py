from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
	path("team_create/", views.TeamCreateView.as_view(), name="team_create"),
	path("team_join/", views.TeamJoinView.as_view(), name="team_join"),
	path("team_list/", views.TeamListView.as_view(), name="team_list"),
]