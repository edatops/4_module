from django.urls import path
from .views import ds
urlpatterns = [
    path('', ds)
]