from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from schedule.models import Schedule


# Create your views here.

class ScheduleView(LoginRequiredMixin, ListView):
    model = Schedule
    context_object_name = 'my_schedules'
    template_name = 'schedule.html'


    def get_queryset(self):
        return Schedule.objects.filter(team__user=self.request.user).order_by('departure_date')




