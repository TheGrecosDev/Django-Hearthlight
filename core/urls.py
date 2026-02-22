from django.urls import path
from core import views

urlpatterns = [
    path("member/<int:id>/", views.member_profile, name="member_profile"),
]