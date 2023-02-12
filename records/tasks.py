from django.core.mail import send_mail
from manicure.celery import app
from .models import Record
from users.models import User
import datetime

@app.task
def record_not_active():
    records = Record.objects.all()
    for record in records:
        if record.date < datetime.datetime.now().date():
            if record.time < datetime.datetime.now().time():
                record.is_active = False
                record.save()

@app.task
def record_created(record_id, user_id):
    """Задача отправки email-уведомлений при успешной записи."""
    record = Record.objects.get(id=record_id)
    user = User.objects.get(id=user_id)
    subject = 'Запись на маникюр'
    message = 'Здравствуйте {} {}!\n\nВы успешно записались на маникюр. Дата {}, время {}'.format(
        user.first_name, user.last_name, record.date, record.time)
    mail_sent = send_mail(subject, message, 'manicurelovet@gmail.com', [user.email])
    return mail_sent

@app.task
def record_canceled(record_id, user_id):
    """Задача отправки email-уведомлений при успешной записи."""
    record = Record.objects.get(id=record_id)
    user = User.objects.get(id=user_id)
    subject = 'Запись на маникюр отменена!'
    message = 'Здравствуйте {} {}!\n\nЗапись на маникюр была отменена. Дата {}, время {}'.format(
        user.first_name, user.last_name, record.date, record.time)
    mail_sent = send_mail(subject, message, 'manicurelovet@gmail.com', [user.email])
    return mail_sent
