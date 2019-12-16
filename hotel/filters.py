from .models import Hotel
import django_filters

class HotelFilter(django_filters.FilterSet):
    product_name = django_filters.CharFilter(lookup_expr='icontains')
    product_price = django_filters.NumberFilter()
    product_price__gt = django_filters.NumberFilter(field_name='product_price', lookup_expr='gt')
    product_price__lt = django_filters.NumberFilter(field_name='product_price', lookup_expr='lt')



    class Meta:
        model = Hotel
        fields = ['product_name', 'product_price', 'vendor_name']








