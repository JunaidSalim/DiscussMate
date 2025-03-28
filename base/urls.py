from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/<str:pk>',views.userProfile,name='profile'),
    path('room/<int:pk>/',views.room,name='room'),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<str:pk>/',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>/',views.deleteRoom,name='delete-room'),
    path('delete-message/<str:pk>/',views.deleteMessage,name='delete-message'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('update-user/',views.updateUser,name='update-user'),
    path('topics/',views.topicsPage,name='topics'),
    path('activity/',views.activityPage,name='activity'),
]