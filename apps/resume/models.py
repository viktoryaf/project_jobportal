from django.db import models
from django.db.models.query import QuerySet

from typing import (
    Optional,
    Any
)

from datetime import datetime


class ResumeQuerySet(QuerySet):
    """VacancyQuerySet."""

    # def get_deleted(self) -> QuerySet['VacancyModel']:
    #     return self.filter(
    #         datetime_deleted__isnull=False
    #     )

    # def get_not_deleted(self) -> QuerySet['VacancyModel']:
    #     return self.filter(
    #         datetime_deleted__isnull=True
    #     )

    # def get_not_equal_updated(self) -> QuerySet['VacancyModel']:
    #     return self.exclude(
    #         datetime_updated=F('datetime_created')
    #     )

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
        # super().delete()


# class Images(models.Model):
#     image = models.ImageField("Примеры работ (портфолио)", max_length=10)


class Resume(models.Model):
    class GenderChoices(models.TextChoices):
        FEMALE = 'Female'
        MALE = 'Male'


    class WorkExperience(models.TextChoices):
        HAVE = 'Есть опыт работы'
        HAVE_NOT = 'Нет опыта работы'


    """Резюме"""

    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    email = models.EmailField(
        "Почта",
        unique=True
    )
    phone = models.CharField(
        "Телефон",
        max_length=11, 
        unique=True
    )
    hometown = models.CharField("Город проживания", max_length=100)
    data_of_birth= models.DateField("Дата рождения")
    age = models.IntegerField("Возраст")
    gender = models.CharField(
        "Пол", 
        max_length=8, 
        choices=GenderChoices.choices, 
        default=GenderChoices.FEMALE
    )
    work_experience = models.CharField(
        "Опыт работы", 
        max_length=35, 
        choices=WorkExperience.choices,
        default=WorkExperience.HAVE
    )

    # image = models.ForeignKey(Images, on_delete=models.CASCADE)
    image = models.ImageField("Примеры работ (портфолио)", max_length=10, blank=True)

    objects = ResumeQuerySet().as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Резюме пользователя"
        verbose_name_plural = "Резюме пользователей"