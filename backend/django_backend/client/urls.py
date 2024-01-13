from django.urls import path
import client.views as views


urlpatterns = [
    path('registration/', views.registration),
    path('client_login/', views.client_login),
    path('is_busy_login/', views.is_busy_login),
    path('is_busy_email/', views.is_busy_email),
    path('training_goals/', views.training_goals),
    path('standard_gym_ticket_offer/', views.standard_gym_ticket_offer),
    path('discount_gym_ticket_offer/', views.discount_gym_ticket_offer),
    path('gyms_list/', views.gyms_list),
    path('change_default_gym/', views.change_default_gym_client),
    path('ordered_classes/', views.get_ordered_classes_client),
    path('ordered_classe_details/', views.get_ordered_gym_classe_details),
    path('client_trenings/', views.get_trainings_client),
    path('trening_details/', views.get_trening_details),
    path('gym_tickets_history/', views.get_gym_tickets_client_history),
    path('gym_tickets_details/', views.get_gym_tickets_details),
    path('client_data/', views.get_client_data),
    path('gym_trainers/', views.get_trainer_by_gym),
    path('gym_classes/', views.get_gym_classes),
    path('free_trainings/', views.get_free_trainings),
    path('free_gym_classes/', views.get_free_gym_classes),
    path('gym_opening_hours/', views.get_gym_opening_hours),
    path('client_can_buy_ticket/', views.check_client_can_buy_gym_ticket),
    path('delete_gym_ticket/', views.delete_gym_ticket),
    path('cancel_ordered_gym_classe/', views.cancel_gym_classe),
    path('reserve_gym_classes/', views.reserve_gym_classes),
    path('buy_items_from_busket/', views.buy_items),
    path('free_gym_classe_details/', views.get_free_gym_classe_details),
    path('price_list/', views.get_price_list),
    path('is_collision_in_basket/', views.check_collision_in_busket)
]
