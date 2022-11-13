from django.contrib import admin

from vacancies.models import (
    VacancyModel,
)


class VacancyAdmin(admin.ModelAdmin):
    model = VacancyModel


admin.site.register(
    VacancyModel, VacancyAdmin
)
