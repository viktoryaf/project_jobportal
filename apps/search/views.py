from rest_framework import (
    generics,
    filters,
)

from vacancies.models import VacancyModel
from vacancies.serializers import VacanciesSerializer


class SearchVacancies(generics.ListAPIView):
    queryset = VacancyModel.objects.all()
    serializer_class = VacanciesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'vacancy_name', 
        'company_name', 
        'salary', 
        'city',
    ]
