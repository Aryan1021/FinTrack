from django.urls import path
from finance.views import home, Homeview

urlpatterns = [
    path('home/', home, name='home'),
    path('', Homeview.as_view(), name='class-home'),
]