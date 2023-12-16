from django.urls import path
import simulation.views as views


urlpatterns = [
    path('all_clients/', views.clients_list),
    path('all_gyms/', views.gyms_list),
    path('all_exercise/', views.exercise_list),
]
