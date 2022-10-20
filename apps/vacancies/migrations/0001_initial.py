# Generated by Django 4.1.2 on 2022-10-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacancy_name', models.CharField(max_length=55, verbose_name='Должность')),
                ('company_name', models.CharField(max_length=55, verbose_name='Название компании')),
                ('salary', models.IntegerField(verbose_name='Доход')),
                ('city', models.CharField(max_length=35, verbose_name='Город')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
