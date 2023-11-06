from django.urls import path
from admissions.views import main

urlpatterns = [
    path("form",main, name="management"),
]