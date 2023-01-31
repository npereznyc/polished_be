import django_filters
from .models import Brand, Polish, User, Review, Favorites



class ReviewFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Polish
        fields = ['name']