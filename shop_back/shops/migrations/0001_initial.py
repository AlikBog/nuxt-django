# Generated by Django 3.2 on 2023-09-13 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Низвание')),
                ('text', models.TextField(verbose_name='Описание')),
                ('made', models.IntegerField(verbose_name='Цена')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('img', models.FileField(upload_to='img/', verbose_name='Картинка')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shops.category', verbose_name='Категория')),
            ],
        ),
    ]
