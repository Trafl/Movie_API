from django.contrib import admin
from django.urls import path

from actors.views import ActorsCreateListAPIView, ActorsRetrieveUpdateDestroyAPIView
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroy
from movies.views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroy.as_view(), name='genres-retrive-update-destroy'),

    path('actors/', ActorsCreateListAPIView.as_view(), name='actors-crete-list'),
    path('actors/<int:pk>/', ActorsRetrieveUpdateDestroyAPIView.as_view(), name='actors-retrive-update-destroy'),

    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movies-retrieve-update-destroy')
]
