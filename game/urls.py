from django.urls import path
from game import views as game_views

urlpatterns = [path("crisscross/", game_views.UserViewSet.as_view())]
