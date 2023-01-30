from rest_framework import serializers
from .models import Brand, Polish, User, Review, Favorites

class PolishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polish
        fields = ('id', 'name', 'brand')

class BrandSerializer(serializers.ModelSerializer):
    polishes=serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name')
    class Meta:
        model = Brand
        fields = ('id', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'polish', 'brand', 'image', 'review')

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id', 'user')