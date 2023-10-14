from django.db import models

class Tovar(models.Model):
    title = models.CharField(max_length=255, verbose_name='Низвание')
    text = models.TextField(verbose_name='Описание')
    made = models.IntegerField(verbose_name='Цена')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    img = models.FileField(upload_to='img/', verbose_name='Картинка')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self):
        return self.name


# Create your models here.
