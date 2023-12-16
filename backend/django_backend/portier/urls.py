from django.urls import path
import portier.views as views

urlpatterns = [
    path('list_clients/', views.list_clients),
    path('find_name_surname/', views.find_client_by_name_surname),
    path('find_phone_number/', views.find_client_by_phone_number),
    path('register_entry/', views.register_entry),
    path('register_leave/', views.register_leave),
]
