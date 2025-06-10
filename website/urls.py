from django.urls import path
from website.views import Home

urlpatterns = [
    path('',Home)
]