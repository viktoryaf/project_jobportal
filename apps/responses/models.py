from django.db import models

from resume.models import Resume


class ResponsesModel(models.Model):
    """ResponsesModel. """

    resume = models.ForeignKey(
        Resume,
        on_delete = models.CASCADE
    )

    class Meta:
        ordering = (
            'id',
        )
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
