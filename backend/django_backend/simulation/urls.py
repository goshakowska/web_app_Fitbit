from django.urls import path
import simulation.views as views


urlpatterns = [
    path('all_clients/', views.clients_list),
]
