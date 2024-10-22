from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroy.as_view(), name='genres-detail-view')
]
