from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),

    
    path('create_room/', views.create_room, name='create_room'),
    path('room_detail/<str:unique_link>/', views.room_detail, name='room_detail'),

    path('archive/', views.archive, name='archive'),

    
    path('detail-text-1/', views.detail_text_1, name='detail-text-1'),
    path('detail-text-2/', views.detail_text_2, name='detail-text-2'),
]
