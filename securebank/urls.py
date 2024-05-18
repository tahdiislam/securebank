from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
]
