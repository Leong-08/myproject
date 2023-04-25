# photoapp/urls.py
#import all the views and functions we need
from django.urls import path
from . import views
from .views import (
    PhotoListView,
    PhotoTagListView,
    PhotoDetailView, 
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView,
    )

app_name = 'photoapp' # this is the namespace for the app

# urlpatterns = [
#     path('', PhotoListView.as_view(), name='list'),
#     path('tag/<slug:tag>/', PhotoTagListView.as_view(), name='tag'),
#     path('photoapp/<int:pk>/', PhotoDetailView.as_view(), name='detail'),
#     path('photoapp/create/', PhotoCreateView.as_view(), name='create'),
#     path('photoapp/<int:pk>/update/', PhotoUpdateView.as_view(), name='update'),
#     path('photoapp/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),
# ]

# urlpatterns = [
#     path('', PhotoListView.as_view(), name='list'),
#     path('create/', PhotoCreateView.as_view(), name='create'),
#     path('<int:pk>/', PhotoDetailView.as_view(), name='detail'),
#     path('<int:pk>/update/', PhotoUpdateView.as_view(), name='update'),
#     path('<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),
#     path('tag/<str:tag>/', PhotoTagListView.as_view(), name='tag'),
# ]

urlpatterns = [
    path('', PhotoListView.as_view(), name='list'),
    path('tag/<slug:tag>/', PhotoTagListView.as_view(), name='tag'),
    path('photoapp/<int:pk>/', PhotoDetailView.as_view(), name='detail'),
    path('photoapp/create/', PhotoCreateView.as_view(), name='create'),
    path('photoapp/update/', PhotoUpdateView.as_view(), name='update'),
    path('photoapp/delete/', PhotoDeleteView.as_view(), name='delete'),
]