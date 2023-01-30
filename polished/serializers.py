from rest_framework import serializers
from .models import Brand, Polish, User, Review, Favorites

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name')

class PolishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polish
        fields = ('name', 'brand')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('user', 'polish', 'brand', 'image', 'review')

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('user')