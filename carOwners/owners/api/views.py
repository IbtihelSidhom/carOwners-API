from rest_framework.generics import ListAPIView
from owners.models import Owner
from .serializers import OwnerSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import filterset 
from django_filters import rest_framework as filters 

class OwnerFilter(filters.FilterSet):
    car_model_year = filters.NumberFilter('car_model_year')
    min_year = filters.NumberFilter(field_name='min_year', method="filter_by_min_year", label='Min year')
    max_year = filters.NumberFilter(field_name='max_year', method="filter_by_max_year", label='Max year')

    class Meta:
        model = Owner
        fields = ['car_model_year', 'min_year', 'max_year']

    def filter_by_min_year(self, queryset, name, value):
        queryset = queryset.filter(car_model_year__gt=value)
        return queryset

    def filter_by_max_year(self, queryset, name, value):
        queryset = queryset.filter(car_model_year__lt=value)
        return queryset

class OwnerListView(ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, ) 
    ordering_fields = ['age', 'car_vin', 'first_name', 'last_name' ] 
    filterset_class = OwnerFilter
    filterset_fields = ('car_model_year', 'min_year', 'max_year')