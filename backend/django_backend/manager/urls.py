from django.urls import path
import manager.views as views

urlpatterns = [
    path('login/', views.manager_login),
]
