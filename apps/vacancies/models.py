from django.db import models


class VacancyModel(models.Model):
    vacancy_name = models.CharField(
        verbose_name='Должность',
        max_length=55
    )
    company_name = models.CharField(
        verbose_name='Название компании',
        max_length=55
    )
    salary = models.IntegerField(
        verbose_name='Доход'
    )
    city = models.CharField(
        verbose_name='Город',
        max_length=35
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=700
    )

    def __str__(self):
        return self.vacancy_name

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'