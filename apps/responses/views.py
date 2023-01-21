from rest_framework.views import APIView

from django.db.models import QuerySet

from abstracts.mixins import (
    ResponseMixin,
    ValidationMixin,
)

from vacancies.serializers import VacanciesSerializer

from responses.models import ResponsesModel


class ResponsesAPIView(
    ValidationMixin,
    ResponseMixin,
    APIView
):
    """VacanciesViewSet."""

    serializer_class = VacanciesSerializer
    model = ResponsesModel
    
    def get(self, request):
        queryset: QuerySet[ResponsesModel] = \
            ResponsesModel.objects.all()
        serializer: VacanciesSerializer = VacanciesSerializer(
            instance=queryset, 
            many=True 
        )
        return self.get_json_response(serializer.data)


class ApplyForJobAPIView(APIView):
    """
    Откликнуться на вакансию.
    """

    