from django.db import models
import uuid
from game import constants as game_constants


class Manager(models.Manager):
    def dfilter(self, *args, **kwargs):
        return self.filter(is_deleted=False, **kwargs)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def delete(self):
        self.is_deleted = True
        self.save(update_fields=["is_deleted"])

    objects = Manager()

    class Meta:
        abstract = True


class UserDetail(BaseModel):
    user_id = models.UUIDField(db_index=True, default=uuid.uuid4)
    user_name = models.CharField(max_length=200)


class GameDetails(BaseModel):
    user = models.ForeignKey(
        "UserDetail", related_name="user_detail", on_delete=models.PROTECT
    )
    game_id = models.UUIDField(db_index=True, default=uuid.uuid4)
    q1 = models.CharField(
        max_length=10,
        choices=game_constants.ALLOWED_CHOICES,
        default=game_constants.NO_MOVE,
    )
    q2 = models.CharField(
        max_length=10,
        choices=game_constants.ALLOWED_CHOICES,
        default=game_constants.NO_MOVE,
    )
    q3 = models.CharField(
        max_length=10,
        choices=game_constants.ALLOWED_CHOICES,
        default=game_constants.NO_MOVE,
    )
    q4 = models.CharField(
        max_length=10,
        choices=game_constants.ALLOWED_CHOICES,
        default=game_constants.NO_MOVE,
    )
    q5 = models.CharField(
        max_length=10,
        choices=game_constants.ALLOWED_CHOICES,
        default=game_constants.NO_MOVE,
    )
    q6 = models.CharField(
        max_length=10,
        choices=game_constants.ALLOWED_CHOICES,
        default=game_constants.NO_MOVE,
    )
    q7 = models.CharField(
        max_length=10,
        choices=game_constants.ALLOWED_CHOICES,
        default=game_constants.NO_MOVE,
    )
    q8 = models.CharField(
        max_length=10,
        choices=game_constants.ALLOWED_CHOICES,
        default=game_constants.NO_MOVE,
    )
    q9 = models.CharField(
        max_length=10,
        choices=game_constants.ALLOWED_CHOICES,
        default=game_constants.NO_MOVE,
    )
    winner = models.CharField(
        max_length=10,
        choices=game_constants.ALLOWED_WINNER,
        default=game_constants.DRAW,
    )
