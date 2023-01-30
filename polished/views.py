from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BrandSerializer, PolishSerializer, UserSerializer, ReviewSerializer, FavoritesSerializer
from .models import Brand, Polish, User, Review, Favorites

# Create your views here.
class PolishView(viewsets.ModelViewSet):
    serializer_class = PolishSerializer
    queryset = Polish.objects.all()

class Reviews(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     polish = self.request.GET.get('polish')
    #     if polish != None:
    #         context['polishes'] = Polish.objects.filter(polish__icontains=polish)
    #         context ['header'] 

