from django.contrib import admin
from django.urls import path

from actors.views import ActorsCreateListAPIView, ActorsRetrieveUpdateDestroyAPIView
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroy
from movies.views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView
from reviews.views import ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name='genres-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroy.as_view(), name='genres-retrieve-update-destroy'),

    path('actors/', ActorsCreateListAPIView.as_view(), name='actors-crete-list'),
    path('actors/<int:pk>/', ActorsRetrieveUpdateDestroyAPIView.as_view(), name='actors-retrieve-update-destroy'),

    path('movies/', MovieListCreateAPIView.as_view(), name='movies-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movies-retrieve-update-destroy'),

    path('reviews/', ReviewListCreateAPIView.as_view(), name='reviews-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='reviews-retrieve-update-destroy')
]
