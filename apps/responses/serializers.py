from responses.models import ResponsesModel

from rest_framework.serializers import (
    ModelSerializer,
    CharField,
)


class ResponsesSerializer(ModelSerializer):
    """ResponsesSerializer. """

    resume = CharField(required=False)

    class Meta:
        model = ResponsesModel
        fields = (
            'id',
            'name',
            'surname',
            'phone',
        )