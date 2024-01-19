from django.urls import path
import trainer.views as views

urlpatterns = [
    path('timetable/', views.timetable),
    path('describe_client/', views.describe_client),
    path('describe_group_class/', views.describe_group_class),
    path('incoming_training/', views.incoming_training),
    path('add_exercise/', views.add_exercise_to_training),
    path('all_exercises/', views.all_exercises),
    path('save_exercises/', views.save_exercise_to_training),
]
