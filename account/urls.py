from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.baseView, name='base'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile-update/', views.profileUpdate, name='profile-update'),
    path('profile-change-permission/<int:pk>/program/<int:pk2>', views.dummyView, name='profile-change-permissions'),
    path('profile-list/', views.profileList, name='profile-list'),
    path('access-denied/', views.accessDenied, name='access-denied'),
    path('user-profile/', views.userProfile, name='user-profile'),
]