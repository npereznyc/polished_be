from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import BrandSerializer, PolishSerializer, UserSerializer, ReviewSerializer, FavoritesSerializer
from .models import Brand, Polish, User, Review, Favorites
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.
class PolishList(viewsets.ModelViewSet):
    serializer_class = PolishSerializer
    queryset = Polish.objects.all()

class Reviews(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
   
class OnePolish(generics.ListAPIView):
    serializer_class = PolishSerializer
    queryset = Polish.objects.all()

class PolishReviews(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class=ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('polish.pk'
    ) #THIS IS NOT WORKING
  