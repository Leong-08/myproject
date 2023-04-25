# users/urls.py

# import all the necessary modules
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import SignUpView, LoginView

# app_name
app_name = 'users'

# urlpatterns
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    # logout view
    path('logout/', LogoutView.as_view(), name='logout'),
]