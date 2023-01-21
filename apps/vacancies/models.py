from django.db import models
from django.db.models.query import QuerySet
from django.db.models import F

from typing import Any
from datetime import datetime


class VacancyQuerySet(QuerySet):
    """VacancyQuerySet."""

    def get_deleted(self) -> QuerySet['VacancyModel']:
        return self.filter(
            datetime_deleted__isnull=False
        )

    def get_not_deleted(self) -> QuerySet['VacancyModel']:
        return self.filter(
            datetime_deleted__isnull=True
        )

    def get_not_equal_updated(self) -> QuerySet['VacancyModel']:
        return self.exclude(
            datetime_updated=F('datetime_created')
        )

    # def get_obj(self, id) -> Optional['VacancyModel']:
    #     try:
    #         return self.get(
    #             id=id
    #         )
    #     except VacancyModel.DoesNotExist:
    #         return None

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.datetime_deleted = datetime.now()
        self.save(
            update_field=['datetime_deleted']
        )


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

    objects = VacancyQuerySet().as_manager()

    class Meta:
        ordering = (
            'id',
        )
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'