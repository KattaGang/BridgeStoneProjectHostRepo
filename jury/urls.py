from django.urls import include, path
from . import views

urlpatterns = [
    path('jury/idea-list/', views.juryIdeaList, name='jury-idea-list'),
    path('jury/idea-accept/<int:pk>/', views.ideaAccept, name='idea-accept'),
    path('jury/idea-reject/<int:pk>/', views.ideaReject, name='idea-reject'),
    path('jury/idea-put-on-hold/<int:pk>/', views.ideaPutOnHold, name='idea-put-on-hold'),
    path('idea-change-status/<int:pk>/', views.ideaChangeStatus, name='idea-change-status'),
]
