from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from django.db.models import QuerySet

from resume.models import Resume
from resume.serializers import (
    ResumeListSerializer,
    ResumeSerializer
)

from abstracts.mixins import (
    ResponseMixin,
    ValidationMixin,
)


class ResumeListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class ResumeListAPIView(
    ValidationMixin,
    ResponseMixin,
    APIView
):
    serializer_class = ResumeListSerializer
    pagination_class = ResumeListPagination
    model = Resume
    
    def get(self, request: Request) -> Response:   
        queryset: QuerySet[Resume] = \
            Resume.objects.all()
        serializer: ResumeSerializer = ResumeSerializer(
            instance=queryset, 
            many=True 
        )
        return self.get_json_response(serializer.data)


class ResumeAPIView(
    ValidationMixin,
    ResponseMixin,
    APIView
):
    
    def get(self, request: Request, id) -> Response: 
        queryset: QuerySet[Resume] = \
            Resume.objects.filter(id=id)

        serializer: ResumeSerializer = ResumeSerializer(
                instance=queryset, 
                many=True 
            )
        return self.get_json_response(serializer.data)

    def post(self, request, id):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.get_json_response(
                {
                    'status': 'success',
                    'message': 'Резюме было создано', 
                    'data': serializer.data
                }, 
                status=status.HTTP_200_OK
            )
        else:
            return self.get_json_response(
                {
                    'error': 'error',
                    'message': 'Резюме не было создано',
                    'data': serializer.errors
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request: Request, id) -> Response:
        obj: Resume = Resume.objects.get(id=id)
        serializer: ResumeSerializer = \
            ResumeSerializer(
                obj, 
                data=request.data
            )

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
        queryset: QuerySet[Resume] = \
            Resume.objects.get(id=id)
        obj: Resume = self.get_obj_if_exists_raise_if_doesnt(
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
                'message': 'Объект был удален',
                'payload': {
                    'obj_id': f'{obj.id}',
                }
            }
        )