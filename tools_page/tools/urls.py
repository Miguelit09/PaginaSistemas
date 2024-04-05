
from django.urls import path
from . import views

urlpatterns = [
    path('create_database/', views.create_database, name="create_database"),
    path('library/', views.library, name="library"),
    path('search_tools/', views.search_tools, name="search_tools"),
    path('get_tool/<int:tool_id>', views.get_tool, name="get_tool"),
]
