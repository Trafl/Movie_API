from django.contrib import admin
from django.urls import path

from actors.views import ActorsCreateListAPIView, ActorsRetrieveUpdateDestroyAPIView
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroy.as_view(), name='genres-retrive-update-destroy'),

    path('actors/', ActorsCreateListAPIView.as_view(), name='actors-crete-list'),
    path('actors/<int:pk>/', ActorsRetrieveUpdateDestroyAPIView.as_view(), name='actors-retrive-update-destroy')
]
