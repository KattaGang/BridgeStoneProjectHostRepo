from django.urls import path, include
from . import views

urlpatterns = [
    
    path('program-create/', views.programCreate, name='program-create'),
    path('program-update/<int:pk>/', views.programUpdate, name='program-update'),
    path('program-delete/<int:pk>/', views.programDelete, name='program-delete'),


    path('program/<int:pk>/', views.programView, name='program'),
    path('program-list/', views.programList, name='program-list'),
    path('program-participants/<int:pk>/', views.dummyView, name='program-participants'),
    path('program-ideas/<int:pk>/', views.dummyView, name='program-ideas'),
    


    path('business-unit-create/', views.dummyView, name='business-unit-create'),
    path('business-unit-update/<int:pk>/', views.dummyView, name='business-unit-update'),
    path('business-unit/<int:pk>/', views.dummyView, name='business-unit'),
    path('business-unit-list/', views.dummyView, name='business-unit-list'),
    path('business-unit-settings/<int:pk>/', views.dummyView, name='business-unit-settings'),
    path('business-unit-jury/<int:pk>/', views.dummyView, name='business-unit-jury'),
    path('business-unit-delete/<int:pk>/', views.dummyView, name='business-unit-delete'),
    path('business-unit/<int:pk>/make-jury/<int:pk2>/', views.dummyView, name='business-unit-make-jury'),
]
