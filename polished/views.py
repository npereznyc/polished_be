from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BrandSerializer, PolishSerializer, UserSerializer, ReviewSerializer, FavoritesSerializer
from .models import Brand, Polish, User, Review, Favorites

# Create your views here.
class PolishView(viewsets.ModelViewSet):
    serializer_class = PolishSerializer
    queryset = Polish.objects.all()