from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import BaseModel

"""Сериализатор"""


class BaseModelSerializer(ModelSerializer):
    cpc = serializers.DecimalField(max_digits=19,
                                   decimal_places=2,
                                   read_only=True)
    cpm = serializers.DecimalField(max_digits=19,
                                   decimal_places=2,
                                   read_only=True)

    class Meta:
        model = BaseModel
        fields = '__all__'
