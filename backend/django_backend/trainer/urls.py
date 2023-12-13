from django.urls import path
import trainer.views as views

urlpatterns = [
    path('timetable/', views.timetable),
]
