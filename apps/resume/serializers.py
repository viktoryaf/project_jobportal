from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.Serializer):
    class Meta:
        model = Resume
        fields = (
            'name', 
            'surname', 
            'phone',
        )