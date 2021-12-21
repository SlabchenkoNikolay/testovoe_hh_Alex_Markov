from django.urls import path

from api.views import BaseModelView

urlpatterns = [
    path('counter/', BaseModelView.as_view(), name='Счетчик'),
]
