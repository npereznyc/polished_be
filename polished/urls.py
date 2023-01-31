from django.urls import path
from django.views.generic import TemplateView

app_name='polished'

urlpatterns= [
    path('', TemplateView.as_view(template_name='polished/index.html')),
]