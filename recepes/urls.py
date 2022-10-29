from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    # path('specific/<int:recipe>/',views.specific),
    path('search/',views.search, name="search"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
]

