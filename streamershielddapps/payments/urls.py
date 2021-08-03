# payments/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('pay/', views.PayView.as_view(), name='pay'),
    path('config/', views.stripe_config),
    path('config2/', views.stripe_config2),
    path('create-checkout-session/', views.create_checkout_session), 
    path('create-checkout-session2/', views.create_checkout_session2), 
    path('success/', views.SuccessView.as_view()), 
    path('cancelled/', views.CancelledView.as_view()),
    path('webhook/', views.stripe_webhook),
]