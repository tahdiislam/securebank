from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.UserUpdateView.as_view(), name='profile'),
    path('change-password/', views.change_pass, name='change_password')
]
