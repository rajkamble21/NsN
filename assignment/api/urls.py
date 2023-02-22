
from django.contrib import admin
from django.urls import path

from api import views
urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('clients/', views.ClientList.as_view(), name='client_list'),
    path('works/', views.WorkList.as_view(), name="works"),
    path('artistsworks/', views.ArtistWorksList.as_view(), name='artist_works_list'),
    path('works/filter/', views.WorkTypeList.as_view(), name='work_filter'),
]