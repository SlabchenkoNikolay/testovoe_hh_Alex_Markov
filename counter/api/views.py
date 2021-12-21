from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from api.filters import Filter
from api.models import BaseModel
from api.serializers import BaseModelSerializer


class BaseModelView(ListCreateAPIView):
    queryset = BaseModel.objects.all()
    serializer_class = BaseModelSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = Filter
    filterset_fields = ('date',)
    ordering_fields = '__all__'

    delete_response = {
        'status': status.HTTP_204_NO_CONTENT,
        'data': 'Данные успешно удалены'
    }

    def delete(self, request, *args, **kwargs):
        response = self.delete_response
        self.queryset.delete()
        return Response(response, status=status.HTTP_204_NO_CONTENT)
