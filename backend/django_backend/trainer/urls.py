from django.urls import path
import trainer.views as views

urlpatterns = [
    path('timetable/', views.timetable),
    path('describe_client/', views.describe_client),
    path('describe_group_class/', views.describe_group_class),
    path('incoming_training/', views.incoming_training)
]
