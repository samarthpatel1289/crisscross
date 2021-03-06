# Generated by Django 3.2.1 on 2021-05-05 17:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "user_id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                ("user_name", models.CharField(max_length=200)),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="GameDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "game_id",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
                ),
                (
                    "q1",
                    models.CharField(
                        choices=[("-1", "-1"), ("1", "1"), ("0", "0")], max_length=10
                    ),
                ),
                (
                    "q2",
                    models.CharField(
                        choices=[("-1", "-1"), ("1", "1"), ("0", "0")], max_length=10
                    ),
                ),
                (
                    "q3",
                    models.CharField(
                        choices=[("-1", "-1"), ("1", "1"), ("0", "0")], max_length=10
                    ),
                ),
                (
                    "q4",
                    models.CharField(
                        choices=[("-1", "-1"), ("1", "1"), ("0", "0")], max_length=10
                    ),
                ),
                (
                    "q5",
                    models.CharField(
                        choices=[("-1", "-1"), ("1", "1"), ("0", "0")], max_length=10
                    ),
                ),
                (
                    "q6",
                    models.CharField(
                        choices=[("-1", "-1"), ("1", "1"), ("0", "0")], max_length=10
                    ),
                ),
                (
                    "q7",
                    models.CharField(
                        choices=[("-1", "-1"), ("1", "1"), ("0", "0")], max_length=10
                    ),
                ),
                (
                    "q8",
                    models.CharField(
                        choices=[("-1", "-1"), ("1", "1"), ("0", "0")], max_length=10
                    ),
                ),
                (
                    "q9",
                    models.CharField(
                        choices=[("-1", "-1"), ("1", "1"), ("0", "0")], max_length=10
                    ),
                ),
                (
                    "winner",
                    models.CharField(
                        choices=[("-1", "-1"), ("1", "1"), ("0", "0")], max_length=10
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_detail",
                        to="game.userdetail",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
    ]
