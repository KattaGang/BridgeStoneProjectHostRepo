from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('admin-panel/', views.adminPanel, name='admin-panel'),
    path('admin-panel/program/<int:pk>/', views.dummyView, name='admin-project-panel'),
]
