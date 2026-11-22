from .views import ScheduleView
from django.urls import path

urlpatterns = [
    path('', ScheduleView.as_view(), name='my_schedule'),
]