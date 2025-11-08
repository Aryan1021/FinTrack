from django.urls import path
from finance.views import home

urlpatterns = [
    path('', home, name='home'),
]