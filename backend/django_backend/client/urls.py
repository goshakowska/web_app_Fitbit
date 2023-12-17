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
    path('change_default_gym/', views.change_default_gym_client),
    path('ordered_classes/', views.get_ordered_classes_client),
    path('client_trenings/', views.get_trenings_client),
    path('trening_details/', views.get_trening_details),
    path('gym_tickets_history/', views.get_gym_tickets_client_history),
    path('gym_tickets_details/', views.get_gym_tickets_details),
]
