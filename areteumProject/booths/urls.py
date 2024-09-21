from django.urls import path, include
from .views import *


urlpatterns = [
    path('booth-day1/', BoothDay1ListView.as_view()),
    path('booth-day2/', BoothDay2ListView.as_view()),
    path('booth-detail/<int:booth_id>/', BoothDetailView.as_view()),
    path('booth-search/', SearchBoothView.as_view()),
]