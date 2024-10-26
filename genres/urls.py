from django.urls import path
from . import views

urlpatterns = [

    path('genres/', views.GenreCreateListView.as_view(), name='genres-create-list'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroy.as_view(), name='genres-retrieve-update-destroy')
]
