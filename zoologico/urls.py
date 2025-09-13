from django.urls import path
from zoologico.views import index

urlpatterns = [
    path('', index, name='index'),
]