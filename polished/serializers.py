from rest_framework import serializers
from .models import Brand, Polish, User, Review, Favorites

class PolishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polish
        fields = ('pk', 'name', 'brand')

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    polishes=serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='one_polish')
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