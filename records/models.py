from django.db import models
from users.models import User

class Record(models.Model):
    time = models.TimeField()
    date = models.DateField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    occupied = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.user

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

