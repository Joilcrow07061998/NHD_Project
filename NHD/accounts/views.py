from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from accounts.models import Worker


# Create your views here.

class WorkerView(LoginRequiredMixin, DetailView): # кабинет работника
    model = Worker
    template_name = 'accounts/cabinet.html'
    context_object_name = 'worker'

    def get_object(self, queryset = None):
        return self.request.user.worker


class WorkersListView(LoginRequiredMixin, ListView):    #список работников
    model = Worker
    template_name = 'accounts/workers.html'
    context_object_name = 'workers'

