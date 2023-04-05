from django.urls import path
from .views import *

urlpatterns = [
    path('', coder, name='rsa'),
]
