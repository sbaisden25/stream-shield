from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from streamershielddapps.streamershieldd_base.views import home_view, terms_view, privpol_view, gold_view, diamond_view, about_view

urlpatterns = [
    path('', home_view, name="home"),

    path('termsandconditions/', terms_view, name="terms"),
    
    path('privacypolicy/', privpol_view, name="privpol"),

    path('gold/', gold_view, name="gold_shield"),
    
    path('diamond/', diamond_view, name="diamond_shield"),

    path('about/', about_view, name="about"),

    
]
