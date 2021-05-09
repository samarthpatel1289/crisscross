from rest_framework import views
from game import serializers as game_serializer
from crisscross import utils as crisscross_utils
from game import models as game_models


class UserViewSet(views.APIView):
    def post(self, request):
        serializer_instance = game_serializer.UserSerializer(data=request.data)
        if not serializer_instance.is_valid():
            return crisscross_utils.create_response(serializer_instance.errors, 400)

        user_name = serializer_instance.validated_data.get("user_name")
        user_instance = game_models.UserDetail.objects.create(user_name=user_name)
        return crisscross_utils.create_response(
            {"user_id": user_instance.user_id}, code=200
        )


class GameViewSet(views.APIView):
    def post(self, request, user_id):
        user_instance = game_models.UserDetail.objects.dfilter(user_id=user_id).last()
        game_instance = game_models.GameDetails.objects.create(
            user = user_instance
        )
        return crisscross_utils.create_response(
        {"game_id":game_instance.game_id}, code=200
        )


    def put(self, request, game_id):
        game_instance = game_models.GameDetails.objects.dfilter(game_id=game_id).last()
        serializer_instance = game_serializer.GameSerializer(data=request.data)
        if not serializer_instance.is_valid():
            return crisscross_utils.create_response(serializer_instance.errors, 400)
        
        print(serializer_instance.validated_data.get('game_board'))

        return crisscross_utils.create_response(
        {"game_id":game_instance.game_id}, code=200
        )

