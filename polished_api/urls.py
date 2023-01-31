from django.urls import path
from .views import ReviewList, ReviewDetail, PolishList

app_name = 'blog_api'

urlpatterns = [
    path('', PolishList.as_view(), name='detailcreate'),
    path('<int:pk>/', PolishList.as_view(), name='detailcreate'),
    # path('<int:pk>/', ReviewDetail.as_view(), name='detailcreate'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name ='listcreate')
    
]