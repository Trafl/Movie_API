from django.urls import path
from . import views


urlpatterns = [

    path('reviews/', views.ReviewListCreateAPIView.as_view(), name='reviews-list-create'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyAPIView.as_view(), name='reviews-retrieve-update-destroy')

]
