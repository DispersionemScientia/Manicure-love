from .models import Record
from django import forms

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['time', 'date']
        labels = {'time': 'Время', 'date': 'Дата', 'occupied': 'Занято'}