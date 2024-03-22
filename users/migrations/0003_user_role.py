# Generated by Django 4.2.7 on 2024-03-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'Member'), ('moderator', 'Moderator')], default='member', max_length=15, verbose_name='роль'),
        ),
    ]
