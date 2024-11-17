from django.urls import path
from .views import recommend_jobs


urlpatterns = [
    path("",recommend_jobs)
]
