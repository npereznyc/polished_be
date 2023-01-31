from django.contrib import admin
from .models import Brand, Polish, User, Review, Favorites

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'polish', 'brand', 'image', 'review')
admin.site.register(Review, ReviewAdmin)

class PolishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand')
admin.site.register(Polish, PolishAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Brand, BrandAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
admin.site.register(User, UserAdmin)


class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
admin.site.register(Favorites, FavoritesAdmin)
