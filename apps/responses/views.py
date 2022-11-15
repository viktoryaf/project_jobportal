from django.db.models import QuerySet

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from abstracts.mixins import (
    ResponseMixin,
    ValidationMixin,
)

from responses.serializers import ResponsesSerializer

from responses.models import ResponsesModel


class ResponsesView(
    ValidationMixin,
    ResponseMixin,
    APIView
):
    """VacanciesViewSet."""

    queryset: QuerySet[ResponsesModel] = \
        ResponsesModel.objects.all()

    @action(
        methods=['get'],
        detail=False,
        url_path='list',
        permission_classes=(
            AllowAny,
        )
    )
    def list(self, request: Request) -> Response:

        serializer: ResponsesSerializer = \
            ResponsesSerializer(
                self.queryset,
                many=True
            )
        return self.get_json_response(
            serializer.data
        )