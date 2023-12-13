from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.authPage, name='login'),
    path('authUser/', views.authUser, name='authUser'),

    path('clientsList/', views.clientsList, name='clientsList'),

    path('сlientsGruzis/', views.clientGr, name='сlientsGruzis'),
    path('sendGruz/', views.sendGruz, name='sendGruz'),
    path('clientPage/<int:user_id>/', views.clientPage, name='clientPage'),
    path('sendGruzToClient/<int:gruz_id>/>', views.sendGruzToClient, name='sendGruzToClient'),

    path('logOut/', views.logOut, name='logOut'),




]