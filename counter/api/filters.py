from django_filters import filters
from django_filters.rest_framework import FilterSet

from api.models import BaseModel

"""Диапазон даты для поиска"""
class Filter(FilterSet):
    from_date = filters.DateFilter(field_name='date',
                                   lookup_expr='gte',
                                   label='От')
    to_date = filters.DateFilter(field_name='date',
                                 lookup_expr='lte',
                                 label='До')
    date_range = filters.DateRangeFilter(field_name='date',
                                         label='Период')

    class Meta:
        model = BaseModel
        fields = ('date',)
