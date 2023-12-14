from django.urls import path
import client.views as views


urlpatterns = [
    path('registration/', views.registration),
    path('client_login/', views.client_login),
    path('is_busy_login/', views.is_busy_login),
    path('training_goals/', views.training_goals),
    path('standard_gym_ticket_offer/', views.standard_gym_ticket_offer),
    path('discount_gym_ticket_offer/', views.discount_gym_ticket_offer),
    path('gyms_list/', views.gyms_list),
]
