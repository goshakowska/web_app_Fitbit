from django.urls import path
import simulation.views as views


urlpatterns = [
    path('all_clients/', views.clients_list),
    path('all_gyms/', views.gyms_list),
    path('all_exercises/', views.exercises_list),
    path('all_trainers/', views.trainers_list),
    path('test_connection/', views.test_connection),
    path('insert_exercise_history/', views.insert_exercise_history),
]
