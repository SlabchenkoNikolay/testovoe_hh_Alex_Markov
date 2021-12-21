from django.test import TestCase

from api.models import BaseModel
from api.serializers import BaseModelSerializer


class BaseModelSerializerTestCase(TestCase):

    """Тест сериализатора"""
    def test_ok(self):
        basemodel_raw_1 = {
            'date': '2021-10-01',
            'views': '10',
            'clicks': '5',
            'cost': '10.00'
        }
        basemodel_raw_2 = {
            'date': '2021-10-02',
            'views': '21',
            'clicks': '6',
            'cost': '102.01'
        }
        basemodel_raw_3 = {
            'date': '2021-09-30',
            'views': '10',
            'clicks': '10',
            'cost': '5.50'
        }
        BaseModel.objects.create(**basemodel_raw_1)
        BaseModel.objects.create(**basemodel_raw_2)
        BaseModel.objects.create(**basemodel_raw_3)

        events = BaseModel.objects.all()
        data = BaseModelSerializer(events, many=True).data
        expected_data = [
            {
                'id': 2,
                'date': '2021-10-02',
                'views': 21,
                'clicks': 6,
                'cost': '102.01',
                'cpc': '17.00',
                'cpm': '4857.62'
            },
            {
                'id': 1,
                'date': '2021-10-01',
                'views': 10,
                'clicks': 5,
                'cost': '10.00',
                'cpc': '2.00',
                'cpm': '1000.00'
            },
            {
                'id': 3,
                'cpc': '0.55',
                'cpm': '550.00',
                'date': '2021-09-30',
                'views': 10,
                'clicks': 10,
                'cost': '5.50'
            }
        ]
        self.assertEqual(expected_data, data)
