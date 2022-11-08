from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
#from rest_framework import generics

from .models import Resume
from .serializers import ResumeSerializer

class ResumeAPIView(APIView):
    serializer_class = ResumeSerializer
    model = Resume
    
    def get(self, request):
        r_get = Resume.objects.all().values()
        return Response({'posts': list(r_get)})

    def post(self, request):
        r_post = Resume.objects.create(
            name=request.data['name'],
            surname=request.data['surname'],
            age=request.data['age']
        )
        return Response({'posts': model_to_dict(r_post)})

