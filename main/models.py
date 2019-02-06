from django.db import models
from django.contrib.auth.models import User, UserManager
from django.utils import timezone
# import datetime


class UserIWM(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Пользователь')
    phone = models.CharField(max_length=100, unique=True, verbose_name='Телефон')
    photo = models.ImageField(upload_to='users_photo/', blank=True, verbose_name='Фото')
    is_parent = models.BooleanField(
        default=False,
        help_text='Укажите если Вы являетесь родителем.',
        verbose_name='Родитель?'
    )

    def __str__(self):
        return self.owner.last_name + ' ' + self.owner.first_name


class IWM(User):
    photo = models.ImageField(upload_to='users_photo/', blank=True, verbose_name='Фото')
    is_parent = models.BooleanField(
        default=False,
        help_text='Укажите если Вы являетесь родителем.',
        verbose_name='Родитель?'
    )

    objects = UserManager()

    phone = models.CharField(max_length=100, unique=True, verbose_name='Телефон')
    # def get_full_name(self):
    #     """
    #     Возвращает полное имя и фамилию
    #     """
    #     full_name = f'self.last_name self.first_name'
    #     print(full_name)
    #     return full_name.strip()

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Tasks(models.Model):
    request = models.CharField(max_length=100, unique=False)
    tasks = models.CharField(max_length=150,unique=True)


class Player(models.Model):
    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Developer(models.Model):
    def __str__(self):
        return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Game(models.Model):
    title = models.CharField(max_length=30, null=False, blank=True, unique=False)
    price = models.FloatField(null=False, blank=False, unique=False)
    url = models.URLField(max_length=300, null=False, blank=False, unique=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)


class Transaction(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    paid_amount = models.FloatField()
    timestamp = models.DateField(default=timezone.now)


# class Parents(models.Model):
#     name = models.CharField(max_length=30, verbose_name='Имя')
#     surname = models.CharField(max_length=30, verbose_name='Фамилия')
#     work = models.BooleanField(default=True, verbose_name='Работа')
#     description = models.TextField(verbose_name='Описание')
#
#     class Meta:
#         verbose_name = 'Родитель'
#         verbose_name_plural = 'Родители'
#         ordering = ['surname']
#
#     def __str__(self):
#         return self.surname + ' ' + self.name
#
#
# class Children(models.Model):
#     login = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Логин')
#     mother = models.ForeignKey(Parents, on_delete=models.CASCADE, related_name='Мать', default='', verbose_name='Мать')
#     father = models.ForeignKey(Parents, on_delete=models.CASCADE, related_name='Отец', default='', verbose_name='Отец')
#     name = models.CharField(max_length=30, verbose_name='Имя')
#     surname = models.CharField(max_length=30, verbose_name='Фамилия')
#     birthday = models.DateField(default=datetime.date.today, verbose_name='День рождения')
#     photo = models.ImageField('Фото', upload_to='main/photos', default='', blank=True)
#
#     class Meta:
#         verbose_name = 'Ребенок'
#         verbose_name_plural = 'Дети'
#         ordering = ['surname']
#
#     def __str__(self):
#         return self.surname + ' ' + self.name
