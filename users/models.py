from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson
from services import NULLABLE


def __str__(self):
    return self.email


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    city = models.CharField(max_length=150, verbose_name='Город', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Payment(models.Model):
    TYPE_PAYMENT = [('CASH', 'Наличка'), ('CARD', 'Оплата картой')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment')
    payment_date = models.DateField(verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payment', verbose_name='Оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payment', verbose_name='Оплаченный урок', **NULLABLE)
    amount_payment = models.PositiveIntegerField(verbose_name='сумма оплаты')
    type_payment = models.CharField(max_length=50,  verbose_name='способ оплаты', choices=TYPE_PAYMENT)
    class Meta:
        verbose_name = 'Оплата'
        ordering = ('-payment_date',)

