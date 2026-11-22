from django.contrib import admin
from .forms import WorkerCreateForm
from .models import Worker




# Регистрируем Worker (только здесь, через декоратор)
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    form = WorkerCreateForm
    list_display = ('get_full_name', 'phone_number')

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    get_full_name.short_description = 'ФИО'