from rest_framework import views
from game import serializers as game_serializer
from crisscross import utils as crisscross_utils
from game import models as game_models
from game import constants as game_constants
from game import utils as game_utils
from django.http import Http404


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
        game_instance = game_models.GameDetails.objects.create(user=user_instance)
        return crisscross_utils.create_response(
            {"game_id": game_instance.game_id}, code=200
        )

    def put(self, request, game_id):
        game_instance = game_models.GameDetails.objects.dfilter(game_id=game_id).last()
        if not game_instance:
            raise Http404

        serializer_instance = game_serializer.GameSerializer(data=request.data)
        if not serializer_instance.is_valid():
            return crisscross_utils.create_response(serializer_instance.errors, 400)

        game_board = serializer_instance.validated_data.get("game_board")
        is_winner = game_utils.is_game_over(game_instance)
        if is_winner == game_constants.PLAYER1:
            game_instance.winner = game_constants.PLAYER1
            game_instance.save(update_fields=["winner"])
            return crisscross_utils.create_response(
                {
                    "game_board": game_board,
                    "winner": game_constants.PLAYER1,
                    "result": "You lose!",
                },
                code=200,
            )
        elif is_winner == game_constants.PLAYER2:
            game_instance.winner = game_constants.PLAYER2
            game_instance.save(update_fields=["winner"])
            return crisscross_utils.create_response(
                {
                    "game_board": game_board,
                    "winner": game_constants.PLAYER2,
                    "result": "You are Winner!",
                },
                code=200,
            )

        if game_instance.winner != game_constants.DRAW:
            return crisscross_utils.create_response(
                {
                    "game_board": game_board,
                    "winner": game_instance.winner,
                    "result": "You are Winner!"
                    if game_instance.winner == game_constants.PLAYER2
                    else "You lose!",
                },
                code=200,
            )

        allowed_moves = []
        i = 0
        for game in game_board:
            i = i + 1
            if game == game_constants.NO_MOVE:
                allowed_moves.append(i - 1)

        if allowed_moves:
            random_move = game_utils.get_random_number(allowed_moves)
            game_board[random_move] = game_constants.PLAYER1
        else:
            return crisscross_utils.create_response(
                {
                    "game_board": game_board,
                    "winner": game_constants.DRAW,
                    "result": "Draw Match",
                },
                code=200,
            )

        game_instance.q1 = game_board[0]
        game_instance.q2 = game_board[1]
        game_instance.q3 = game_board[2]
        game_instance.q4 = game_board[3]
        game_instance.q5 = game_board[4]
        game_instance.q6 = game_board[5]
        game_instance.q7 = game_board[6]
        game_instance.q8 = game_board[7]
        game_instance.q9 = game_board[8]

        game_instance.save(
            update_fields=["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9"]
        )

        game_board = [
            str(game_instance.q1),
            str(game_instance.q2),
            str(game_instance.q3),
            str(game_instance.q4),
            str(game_instance.q5),
            str(game_instance.q6),
            str(game_instance.q7),
            str(game_instance.q8),
            str(game_instance.q9),
        ]

        is_winner = game_utils.is_game_over(game_instance)
        if is_winner == game_constants.PLAYER1:
            game_instance.winner = game_constants.PLAYER1
            game_instance.save(update_fields=["winner"])
            return crisscross_utils.create_response(
                {
                    "game_board": game_board,
                    "winner": game_constants.PLAYER1,
                    "result": "You lose!",
                },
                code=200,
            )
        elif is_winner == game_constants.PLAYER2:
            game_instance.winner = game_constants.PLAYER2
            game_instance.save(update_fields=["winner"])
            return crisscross_utils.create_response(
                {
                    "game_board": game_board,
                    "winner": game_constants.PLAYER2,
                    "result": "You are Winner!",
                },
                code=200,
            )

        return crisscross_utils.create_response({"game_board": game_board}, code=200)
