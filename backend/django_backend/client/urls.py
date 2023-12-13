from django.urls import path
import client.views as views


urlpatterns = [
    path('registration/', views.registration),
    path('client_login/', views.client_login),
    path('validate_password/', views.validate_password_client),
]
