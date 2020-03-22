from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('contact/',views.contact,name="contact"),
    path('music/',views.music, name="music"),
    path("musicview/<int:myid>", views.musicView, name="musicview"),
    path("about/", views.about, name="about")
]