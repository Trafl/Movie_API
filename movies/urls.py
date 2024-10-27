from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [

    path('movies/', views.MovieListCreateAPIView.as_view(), name='movies-list-create'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyAPIView.as_view(), name='movies-retrieve-update-destroy'),
    path('movies/stats/', views.MovieStatsView.as_view(), name='movies-stats-views')
]
