from django.urls import path, include
from rest_framework import routers
from polished import views

router = routers.DefaultRouter()
router.register(r'polishes', views.PolishList, 'polishes')
router.register(r'reviews', views.Reviews, 'reviews')



urlpatterns = [
    path('api/', include(router.urls)),
    path('polishes/<int:pk>/', views.OnePolish.as_view(), name='one_polish'),
    # path('polishes/', views.PolishList, name='polishes'),
    path('polishes/<int:pk>/reviews', views.PolishReviews.as_view(), name='polish_review'),
    # path('reviews/', views.Reviews.as_view(), name='reviews')
]