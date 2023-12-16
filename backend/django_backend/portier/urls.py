from django.urls import path
import portier.views as views

urlpatterns = [
    path('list_clients/', views.list_clients),
    path('find_name_surname/', views.find_client_by_name_surname),
]
