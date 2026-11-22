
import uuid

from django import forms
from django.contrib.auth.models import User

from .models import Worker


class WorkerCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, label='Имя')
    last_name = forms.CharField(max_length=150, label='Фамилия')
    patronymic = forms.CharField(max_length=150, label='Отчество', required=False)

    class Meta:
        model = Worker
        fields = ('last_name', 'first_name', 'patronymic', 'phone_number')
        labels = {
            'phone_number': 'Телефон',
        }

    def save(self, commit=True):
        worker = super().save(commit=False)

        first_name = self.cleaned_data['first_name']
        patronymic = self.cleaned_data.get('patronymic')

        if patronymic:
            first_name = f'{first_name} {patronymic}'

        user = User(
            username=f'worker_{uuid.uuid4().hex}',
            first_name=first_name,
            last_name=self.cleaned_data['last_name'],
        )
        user.set_unusable_password()
        user.save()

        # Сигнал автоматически создаёт Worker при сохранении User.
        worker = user.worker
        worker.phone_number = self.cleaned_data['phone_number']

        if commit:
            worker.save()

        return worker
