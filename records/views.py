from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from users.models import User
from .models import Record
from .forms import RecordForm
from .tasks import record_created, record_canceled

class RecordView(ListView):
    model = Record
    template_name = 'records/records.html'
    context_object_name = 'records'

    def get_queryset(self):
        return Record.objects.filter(is_active=True).order_by('date', 'time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['months'] = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
                             'Октябрь', 'Ноябрь', 'Декабрь']
        context['days'] = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        return context

class RecordAllView(ListView):
    model = Record
    template_name = 'records/records_all.html'
    context_object_name = 'records'

    def get_queryset(self):
        return Record.objects.all()




class RecordAddView(CreateView):
    template_name = 'records/record_add.html'
    form_class = RecordForm
    success_url = reverse_lazy('records:records')

class ShowRecordView(DetailView):
    model = Record
    template_name = 'records/show_record.html'
    context_object_name = 'record'

class DeleteRecordView(DeleteView):
    model = Record
    template_name = 'records/delete_record.html'
    success_url = reverse_lazy('users:administration')

def home(request):
    return render(request, 'records/home.html')

''' запись становится занята текущем пользователем и отправка сообщения об успешной записи ему на почту '''
def record_occupied(request, record_pk):
    record = Record.objects.get(id=record_pk)

    if request.user.is_authenticated and not record.user:
        record.user = User.objects.get(id=request.user.id)
        record.occupied = True
        record.save()
        record_created.delay(record_id=record_pk, user_id=request.user.id)
        return redirect('records:records')

# отмена записи
def cansel_record(request, record_pk):
    record = Record.objects.get(id=record_pk)
    record.occupied = False
    record.user = None
    record.save()
    record_canceled(record_id=record_pk, user_id=request.user.id)
    return redirect('records:home')

