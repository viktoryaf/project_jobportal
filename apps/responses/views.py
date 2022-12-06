from rest_framework.views import APIView
from rest_framework.response import Response

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
        r_get = ResponsesModel.objects.all().values()
        return Response({'posts': list(r_get)})


class ApplyForJobAPIView(APIView):
    """
    Откликнуться на вакансию.
    """

    