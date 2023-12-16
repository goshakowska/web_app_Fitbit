from django.urls import path
import portier.views as views

urlpatterns = [
    path('list_clients/', views.list_clients),
]
