from django.urls import path 
from .views import create_view, list_view, detail_view


urlpatterns = [
    path('', list_view, name='publication-list'),
    path('create/', create_view, name='create-post'),
    path('<int:id>/detail/', detail_view, name='publication-detail')
]
