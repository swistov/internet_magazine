# Generated by Django 2.1.5 on 2019-02-02 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useriwm',
            name='is_parent',
            field=models.BooleanField(default=False, help_text='Укажите если Вы являетесь родителем.', verbose_name='Родитель?'),
        ),
        migrations.AlterField(
            model_name='useriwm',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Пользователь', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='useriwm',
            name='phone',
            field=models.CharField(max_length=100, unique=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='useriwm',
            name='photo',
            field=models.ImageField(upload_to='users_photo/', verbose_name='Фото'),
        ),
    ]