from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="user-home"),
    path('<int:user_id>/', views.user, name='user-id'),
]