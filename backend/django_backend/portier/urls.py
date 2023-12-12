from django.urls import path
import portier.views as views

urlpatterns = [
    path('login/', views.portier_login),
]
