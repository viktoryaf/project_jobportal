from django.db.models import QuerySet
from django.forms import model_to_dict

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
# from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import status

from abstracts.mixins import (
    ResponseMixin,
    ValidationMixin,
)

from vacancies.serializers import (
    VacanciesSerializer,
    VacancySerializer,
)

from vacancies.models import VacancyModel


class VacanciesView(
    ValidationMixin,
    ResponseMixin,
    APIView
):
    """VacanciesView."""

    serializer_class = VacanciesSerializer
    model = VacancyModel

    def get(self, request: Request) -> Response:   
        queryset: QuerySet[VacancyModel] = \
            VacancyModel.objects.all()
        serializer_for_queryset = VacanciesSerializer(
            instance=queryset, # Передаём набор записей
            many=True # Указываем, что на вход подаётся именно набор записей
        )
        return self.get_json_response(serializer_for_queryset.data)


class VacancyView(
    ValidationMixin,
    ResponseMixin,
    APIView
):
    """VacancyView. """
    serializer_class = VacancySerializer
    model = VacancyModel

    def get(self, request: Request, id) -> Response: 
        queryset: QuerySet[VacancyModel] = \
            VacancyModel.objects.filter(id=id)

        serializer_for_queryset = VacancySerializer(
                instance=queryset, # Передаём набор записей
                many=True # Указываем, что на вход подаётся именно набор записей
            )
        return self.get_json_response(serializer_for_queryset.data)

    def post(self, request, id):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

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
                    'message': 'Обьект не был обновлен',
                    'payload': serializer.errors
                }
            )
        serializer.save()

        return self.get_json_response(
            {
                'message': 'Обьект был обновлен',
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
        obj.delete()

        return self.get_json_response(
            {
                'message': 'Объект был удален',
                'payload': {
                    'obj_id': f'{obj.id}',
                    # 'obj_deleted': f'{obj.datetime_deleted}',
                }
            }
        )