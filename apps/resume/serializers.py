from rest_framework import serializers
from .models import Resume

class ResumeListSerializer(serializers.Serializer):

    name = serializers.CharField(required=False)
    surname = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    work_experience = serializers.CharField(required=False)
    class Meta:
        model = Resume
        fields = (
            'id',
            'name', 
            'surname', 
            'age',
            'work_experience'
        )

    def create(self, validated_data):
        return Resume.objects.create(**validated_data)

class ResumeSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    surname = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)
    hometown = serializers.CharField(required=False)
    data_of_birth = serializers.DateField(required=False)
    age = serializers.IntegerField(required=False)
    gender = serializers.CharField(required=False)
    work_experience = serializers.CharField(required=False)
    image = serializers.ImageField(required=True)
    class Meta:
        model = Resume
        fields = (
            'id',
            'name', 
            'surname', 
            'email',
            'phone',
            'data_of_birth',
            'age',
            'gender',
            'work_experience',
            'image'
        )

    def create(self, validated_data):
        return Resume.objects.create(**validated_data)
