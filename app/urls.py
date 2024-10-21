from tkinter.font import names

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_list_view, name= 'genre-list'),
]
