from rest_framework import (
    generics,
    filters,
)
from rest_framework.pagination import PageNumberPagination

from vacancies.models import VacancyModel
from vacancies.serializers import VacanciesSerializer

from django.db.models import Q


class SearchVacanciesPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class SearchVacancies(generics.ListAPIView):
    queryset = VacancyModel.objects.all()
    serializer_class = VacanciesSerializer
    pagination_class = SearchVacanciesPagination
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'vacancy_name', 
        'company_name', 
        'salary', 
        'city',
    ]

    def form_valid(self, form):
        request = VacancyModel.objects.filter(Q(self.request is True))
        if not request.is_valid():
            return self.get_json_response(
                {
                    'message': f'По запросу {request} ничего не найдено',
                    'payload': request.errors
                }
            )

        return self.get_json_response(
            {
                'data': request
            }
        )