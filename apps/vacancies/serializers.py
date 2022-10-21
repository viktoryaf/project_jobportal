from vacancies.models import VacancyModel

from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    IntegerField
)


class VacanciesSerializer(ModelSerializer):
    """VacanciesSerializer. """

    vacancy_name = CharField(required=False)
    company_name = CharField(required=False)
    salary = IntegerField(required=False)
    city = CharField(required=False)

    class Meta:
        model = VacancyModel
        fields = (
            'vacancy_name',
            'company_name',
            'salary',
            'city'
        )


class VacancySerializer(ModelSerializer):
    """VacancySerializer. """

    vacancy_name = CharField(required=False)
    company_name = CharField(required=False)
    salary = IntegerField(required=False)
    city = CharField(required=False)
    description = CharField(required=False)

    class Meta:
        model = VacancyModel
        fields = (
            'vacancy_name',
            'company_name',
            'salary',
            'city',
            'description'
        )