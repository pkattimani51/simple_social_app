from django.urls import path
from . import views

app_name = 'groups'


urlpatterns = [
    path('', views.ListGroup.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('posts/in/<str:slug>', views.SingleGroup.as_view(), name='single'),
    path('leave/<str:slug>/', views.LeaveGroup.as_view(), name='leave'),
    path('join/<str:slug>/', views.JoinGroup.as_view(), name='join'),
]