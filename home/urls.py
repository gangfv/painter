from django.urls import path
from home.views import HomeView, FormCreteApi

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('form/', FormCreteApi.as_view())
]
