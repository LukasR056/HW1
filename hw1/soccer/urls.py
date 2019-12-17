from django.urls import path

from soccer import views

urlpatterns = [

    path('country/',views.country_list),
    path('country/<int:pk>/',views.country_detail),
    path('club/',views.club_list),
    path('club/<int:pk>/',views.club_detail),
    path('player/',views.player_list),
    path('player/<int:pk>/',views.player_detail),

]