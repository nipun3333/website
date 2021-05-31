from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('facilities', views.facilities, name="facilities"),
    path('products', views.products, name="products"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('about_us', views.about_us, name="about_us"),
]