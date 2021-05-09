from django.urls import path
from game import views as game_views

urlpatterns = [
    path("crisscross/", game_views.UserViewSet.as_view()),
    path("crisscross/<uuid:user_id>/game/",game_views.GameViewSet.as_view()),

    path("crisscross/game/<uuid:game_id>/",game_views.GameViewSet.as_view()),

    ]
