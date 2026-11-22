from django.contrib import admin
from .models import Schedule


admin.site.register(Schedule)

filter_horizontal = ('team',)