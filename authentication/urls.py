from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='index'),
    path('register/', views.register, name='register' ),
    path('login/', views.login, name='login' ),
    path('dashboard/', views.dashboard, name='dashbaord' ),
    path('logout/', views.signout, name='signout' ),
]