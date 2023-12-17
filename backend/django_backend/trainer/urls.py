from django.urls import path
import trainer.views as views

urlpatterns = [
    path('timetable/', views.timetable),
    path('describe_client/', views.describe_client),
    path('describe_group_class/', views.describe_group_class),
    path('incoming_training/', views.incoming_training),
    path('measured_repetition/', views.exercise_measured_repetition_number),
    path('measured_duration/', views.exercise_measured_duration),
    path('add_exercise/', views.add_exercise_to_training),
    path('move_up/', views.move_up_exercise),
    path('move_down/', views.move_down_exercise),
    path('delete_exercise/', views.delete_exercise_from_training),
]
