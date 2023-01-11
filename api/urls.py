from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.getRoutes, name='get-routes'),
    path('ideas/', views.getIdeas, name='get-ideas'),
    path('idea/<int:pk>/', views.getIdea, name='get-idea'),
    path('programs/', views.getPrograms, name='get-programs'),
    path('program/<int:pk>/', views.getProgram, name='get-program'),
    path('business-units/', views.getBusinessUnits, name='get-business-units'),
    path('business-unit/<int:pk>/',
         views.getBusinessUnit, name='get-business-unit'),

    path('get-idea-activity/', views.getIdeaActivity, name='get-idea-activity'),
]
