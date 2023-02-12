
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator

class UserAccountManager(UserManager):

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        extra_fields['telephon_number'] = '00000000000'
        extra_fields['birth_date'] = '1999-01-01'

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    objects = UserAccountManager()
    telephon_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    telephon_number = models.CharField(
        validators=[telephon_number_regex],
        max_length=16,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Номер телефона"
    )
    birth_date = models.DateField(verbose_name="Дата рождения")
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'