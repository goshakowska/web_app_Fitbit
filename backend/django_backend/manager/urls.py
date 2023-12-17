from django.urls import path
import manager.views as views

urlpatterns = [
    path('ticket_popularity_week/', views.ticket_popularity_week),
    path('discount_popularity_week/', views.discount_popularity_week),
]
