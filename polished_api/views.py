from rest_framework import generics
from polished.models import Brand, Polish, User, Review, Favorites
from .serializers import BrandSerializer, PolishSerializer, UserSerializer, ReviewSerializer, FavoritesSerializer

# Create your views here.
class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

class ReviewDetail(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class PolishList(generics.ListAPIView):
    serializer_class = PolishSerializer
    queryset = Polish.objects.all()
   
# class OnePolish(generics.ListAPIView):
#     serializer_class = PolishSerializer
#     queryset = Polish.objects.all()