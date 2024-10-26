from django.urls import path
from . import views

urlpatterns = [

    path('actors/', views.ActorsCreateListAPIView.as_view(), name='actors-crete-list'),
    path('actors/<int:pk>/', views.ActorsRetrieveUpdateDestroyAPIView.as_view(), name='actors-retrieve-update-destroy'),

]
