from rest_framework import (
    generics,
    filters,
)

from vacancies.models import VacancyModel
from vacancies.serializers import VacanciesSerializer

from django.db.models import Q


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

    def form_valid(self, form):
        request = VacancyModel.objects.filter(Q(self.request is True))
        return request
