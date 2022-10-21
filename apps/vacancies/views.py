from django.shortcuts import render

from django.db.models import QuerySet

from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

# from abstracts.mixins import (
#     ResponseMixin,
#     ValidationMixin,
# )

from vacancies.serializers import (
    VacanciesSerializer,
    VacancySerializer,
)

from vacancies.models import VacancyModel


class VacanciesViewSet(
    # ValidationMixin,
    # ResponseMixin,
    ViewSet
):
    """VacanciesViewSet."""

    queryset: QuerySet[VacancyModel] = \
        VacancyModel.objects.all()

    @action(
        methods=['get'],
        detail=False,
        url_path='list',
        permission_classes=(
            AllowAny,
        )
    )
    def list(self, request: Request) -> Response:

        serializer: VacanciesSerializer = \
            VacanciesSerializer(
                self.queryset,
                many=True
            )
        return self.get_json_response(
            serializer.data
        )


class VacancyViewSet(ViewSet):
    """VacancyViewSet. """

    queryset: QuerySet[VacancyModel] = \
        VacancyModel.objects.filter(id=id)

    @action(
        methods=['get'],
        detail=False,
        url_path='list',
        permission_classes=(
            AllowAny,
        )
    )
    def list(self, request: Request) -> Response:

        serializer: VacancySerializer = \
            VacancySerializer(
                self.queryset,
                many=True
            )
        return self.get_json_response(
            serializer.data
        )