from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson, NULLABLE
# from services import NULLABLE


class UserRoles(models.TextChoices):
    MEMBER = 'member'
    MODERATOR = 'moderator'


class User(AbstractUser):
    role = models.CharField(max_length=15, verbose_name='роль', choices=UserRoles.choices, default=UserRoles.MEMBER)
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')

    city = models.CharField(max_length=150, verbose_name='Город', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Payment(models.Model):
    TYPE_PAYMENT = [('CASH', 'Наличка'), ('CARD', 'Оплата картой')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment')
    payment_date = models.DateField(verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payment',
                               verbose_name='Оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payment',
                               verbose_name='Оплаченный урок', **NULLABLE)
    payment_amount = models.FloatField(verbose_name='Сумма платежа', **NULLABLE)
    type_payment = models.CharField(max_length=50,  verbose_name='способ оплаты', choices=TYPE_PAYMENT)
    payment_status = models.CharField(default='unpaid', verbose_name='Статус оплаты')
    payment_url = models.TextField(verbose_name='Ссылка на оплату', **NULLABLE)
    session_id = models.CharField(max_length=255, verbose_name='id платежной сессии', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, related_name='paid_course', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, related_name='paid_lesson', **NULLABLE)

    class Meta:
        verbose_name = 'Оплата'
        ordering = ('-payment_date',
                    )



class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='user')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f"{self.user} {self.course}"

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'