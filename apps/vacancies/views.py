from django.db.models import QuerySet

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from abstracts.mixins import (
    ResponseMixin,
    ValidationMixin,
)

from vacancies.serializers import (
    VacanciesSerializer,
    VacancySerializer,
)

from vacancies.models import VacancyModel


class VacanciesViewPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class VacanciesView(
    ValidationMixin,
    ResponseMixin,
    APIView
):
    """VacanciesView."""

    serializer_class = VacanciesSerializer
    pagination_class = VacanciesViewPagination
    model = VacancyModel

    def get(self, request: Request) -> Response:   
        queryset: QuerySet[VacancyModel] = \
            VacancyModel.objects.all()
        serializer: VacancySerializer = VacanciesSerializer(
            instance=queryset, 
            many=True 
        )
        return self.get_json_response(
            {
                'message': '',
                'payload': serializer.data
            }
        )


class VacancyView(
    ValidationMixin,
    ResponseMixin,
    APIView
):
    """VacancyView. """
    serializer_class = VacancySerializer
    model = VacancyModel
    permission_classes = [IsAuthenticated]
    queryset = VacancyModel.objects.all()
    # authentication_classes = (TokenAuthentication, )

    def get(self, request: Request, id) -> Response: 
        queryset: QuerySet[VacancyModel] = \
            VacancyModel.objects.filter(id=id)

        serializer: VacancySerializer = VacancySerializer(
                instance=queryset, 
                many=True 
            )
        return self.get_json_response(
            {
                'message': '',
                'payload': serializer.data
            }
        )

    def post(self, request, id):
        serializer: VacancySerializer = \
            VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.get_json_response(
                {
                    'status': 'success',
                    'message': 'Вакансия была создана', 
                    'data': serializer.data
                }, 
                status=status.HTTP_200_OK
            )
        else:
            return self.get_json_response(
                {
                    'error': 'error',
                    'message': 'Вакансия не была создана',
                    'data': serializer.errors
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request: Request, id) -> Response:
        obj: VacancyModel = VacancyModel.objects.get(id=id)
        serializer: VacanciesSerializer = \
            VacanciesSerializer(
                obj, 
                data=request.data
            )
        # request.data['obj_id'] = obj.id

        if not serializer.is_valid():
            return self.get_json_response(
                {
                    'message': 'Вакансия не была обновлена',
                    'payload': serializer.errors
                }
            )
        serializer.save()

        return self.get_json_response(
            {
                'message': 'Вакансия была обновлена',
                'payload': serializer.data
            }
        )

    def delete(self, request: Request, id) -> Response:
        queryset: QuerySet[VacancyModel] = \
            VacancyModel.objects.get(id=id)
        obj: VacancyModel = self.get_obj_if_exists_raise_if_doesnt(
            queryset,
            id
        )
        if not obj.is_valid():
            return self.get_json_response(
                {
                    'message': 'Несуществующий объект',
                    'payload': obj.errors
                }
            )
        obj.delete()

        return self.get_json_response(
            {
                'message': 'Вакансия была удалена',
                'payload': {
                    'obj_id': f'{obj.id}',
                }
            }
        )