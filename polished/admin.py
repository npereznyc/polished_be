from django.contrib import admin
from .models import Brand, Polish, User, Review, Favorites

# Register your models here.
admin.site.register(Brand)
admin.site.register(Polish)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Favorites)