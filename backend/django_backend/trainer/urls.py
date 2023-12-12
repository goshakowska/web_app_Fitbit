from django.urls import path
import trainer.views as views

urlpatterns = [
    path('login/', views.trainer_login),
]
