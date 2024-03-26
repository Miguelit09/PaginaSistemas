
from django.urls import path, include
from . import views

urlpatterns = [
    path('library/', views.library, name="library"),
    path('item/', views.item, name="item"),
    path('seeker/', views.seeker, name="seeker"),
]
