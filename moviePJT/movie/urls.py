from django.urls import path, include
from movie import views
urlpatterns = [
    path('latest-movies/', views.LatestProductsList.as_view())

]