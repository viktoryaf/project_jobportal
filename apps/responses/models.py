from django.db import models

from vacancies.models import VacancyModel


class ResponsesModel(models.Model):
    """ResponsesModel. """

    resume = models.ForeignKey(
        VacancyModel,
        on_delete = models.CASCADE
    )

    class Meta:
        ordering = (
            'id',
        )
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
