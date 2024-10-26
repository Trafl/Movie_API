from django.contrib import admin
from django.urls import path, include

from actors.views import ActorsCreateListAPIView, ActorsRetrieveUpdateDestroyAPIView
from movies.views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView
from reviews.views import ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/v1/', include('genres.urls')),

    path('api/v1/', include('actors.urls')),

    path('api/v1/', include('movies.urls')),

    path('api/v1/', include('reviews.urls'))

    ]
