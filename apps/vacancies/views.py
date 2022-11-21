from django.db.models import QuerySet
from django.forms import model_to_dict

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
# from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

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

    # queryset: QuerySet[VacancyModel] = \
    #     VacancyModel.objects.all()


    # def destroy(self, request: Request, pk: str) -> Response:

    #     obj: VacancyModel = self.get_obj_if_exists_raise_if_doesnt(
    #         self.queryset,
    #         pk
    #     )
    #     obj.delete()

    #     return self.get_json_response(
    #         {
    #             'message': 'Объект был удален',
    #             'payload': {
    #                 'obj_id': f'{obj.id}',
    #                 'obj_deleted': f'{obj.datetime_deleted}',
    #             }
    #         }
    #     )

    # def create(self, request: Request) -> Response:

    #     serializer: VacanciesSerializer = \
    #         VacanciesSerializer(
    #             data=request.data
    #         )
    #     if not serializer.is_valid:
    #         return self.get_json_response(
    #             {
    #                 'message': 'Обьект не был создан',
    #                 'payload': request.data
    #             }
    #         )
            
    #     serializer.save()

    #     return self.get_json_response(
    #         {
    #             'message': 'Обьект был создан',
    #         }
    #     )

    # def update(self, request: Request, pk: str) -> Response:

    #     obj: VacancyModel = self.get_obj_or_raise(
    #         self.queryset,
    #         pk
    #     )
    #     serializer: VacanciesSerializer = \
    #         VacanciesSerializer(
    #             obj, 
    #             data=request.data
    #         )
    #     request.data['obj_id'] = obj.id

    #     if not serializer.is_valid:
    #         return self.get_json_response(
    #             {
    #                 'message': 'Обьект не был обновлен',
    #                 'payload': request.data
    #             }
    #         )
    #     serializer.save()

    #     return self.get_json_response(
    #         {
    #             'message': 'Обьект был обновлен',
    #             'payload': request.data
    #         }
    #     )


    serializer_class = VacanciesSerializer
    model = VacancyModel
    
    def get(self, request):
        queryset: QuerySet[VacancyModel] = \
            VacancyModel.objects.all().values()
        return Response({'posts': list(queryset)})

    def post(self, request):
        r_post = VacancyModel.objects.create(
            name=request.data['name'],
            password=request.data['password'],
        )
        return Response({'posts': model_to_dict(r_post)})


class VacancyView(APIView):
    """VacancyView. """
    serializer_class = VacancySerializer
    model = VacancyModel

    def get_queryset(self):
        queryset: QuerySet[VacancyModel] = \
            VacancyModel.objects.filter(pk=id)
            # VacancyModel.objects.filter(pk=self.kwargs['id'])
        return queryset

    def post(self, request: Request) -> Response:
        serializer: VacancySerializer = \
            VacancySerializer(
                self.get_queryset,
                many=True
            )
        return Response({'posts': serializer})

