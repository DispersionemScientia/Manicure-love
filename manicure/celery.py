import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manicure.settings')

app = Celery('manicure')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'record_not_active': {
        'task': 'records.tasks.record_not_active',
        'schedule': crontab(minute=0, hour='*/1'),
        # 'schedule': crontab(),
    },
}
