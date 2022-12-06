from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from django.forms import model_to_dict
from django.db.models import QuerySet

#from rest_framework import generics

from resume.models import Resume
from resume.serializers import (
    ResumeListSerializer,
    ResumeSerializer
)

from abstracts.mixins import (
    ResponseMixin,
    ValidationMixin,
)


class ResumeAPIView(
    ValidationMixin,
    ResponseMixin,
    APIView
):
    
    def get(self, request: Request, id) -> Response: 
        queryset: QuerySet[Resume] = \
            Resume.objects.filter(id=id)

        serializer_for_queryset = ResumeSerializer(
                instance=queryset, # Передаём набор записей
                many=True # Указываем, что на вход подаётся именно набор записей
            )
        return self.get_json_response(serializer_for_queryset.data)

    def post(self, request, id):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, id) -> Response:
        obj: Resume = Resume.objects.get(id=id)
        serializer: ResumeSerializer = \
            ResumeSerializer(
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

    def destroy(self, request: Request, id) -> Response:
        queryset: QuerySet[Resume] = \
            Resume.objects.get(id=id)
        obj: Resume = self.get_obj_if_exists_raise_if_doesnt(
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


class ResumeListAPIView(
    ValidationMixin,
    ResponseMixin,
    APIView
):
    serializer_class = ResumeListSerializer
    model = Resume
    
    def get(self, request: Request) -> Response:   
        queryset: QuerySet[Resume] = \
            Resume.objects.all()
        serializer_for_queryset = ResumeSerializer(
            instance=queryset, # Передаём набор записей
            many=True # Указываем, что на вход подаётся именно набор записей
        )
        return self.get_json_response(serializer_for_queryset.data)

    # def post(self, request: Request) -> Response:
    #     serializer: ResumeSerializer = \
    #          ResumeSerializer.create(data=request.data)
    #     if not serializer.is_valid():
    #         return self.get_json_response(
    #             {
    #                 'message': 'Обьект не был создан',
    #                 'payload': request
    #             }
    #         )
            
    #     serializer.save()

    #     return self.get_json_response(
    #         {
    #             'message': 'Обьект был создан',
    #             'post': serializer
    #         }
    #     )

    # def post(self, request):
    #     serializer = ResumeListSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    #     else:
    #         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
