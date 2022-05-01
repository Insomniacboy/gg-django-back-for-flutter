from . import views
from django.urls import path

urlpatterns = [
    path('', views.getRoutes),
    path('info/', views.getInfo),
    path('info/create/', views.createInfo),
    path('info/<str:pk>/update/', views.updateInfo),
    path('info/<str:pk>/delete/', views.deleteInfo),
    path('info/<str:pk>/', views.getSingleInfo),
    path('login/', views.UserAuth.as_view()),
    path('register/', views.UserRegister.as_view()),
]
