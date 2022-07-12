from django.urls import path
from .views import MainView
from django.views.generic import TemplateView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('customs/', TemplateView.as_view(template_name='services-details.html'), name='customs')
]