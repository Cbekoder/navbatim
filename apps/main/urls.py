from django.urls import path
from .views import coming_soon


urlpatterns = [
    path('countdown/', coming_soon, name='coming_soon'),
]