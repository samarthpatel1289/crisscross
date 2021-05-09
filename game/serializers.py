from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=200, required=True)


class GameSerializer(serializers.Serializer):
    game_board = serializers.ListField()
