# Generated by Django 3.2.1 on 2021-05-09 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("game", "0005_auto_20210509_0505")]

    operations = [
        migrations.AlterField(
            model_name="gamedetails",
            name="q1",
            field=models.CharField(
                choices=[("-1", "-1"), ("1", "1"), ("0", "0")],
                default="0",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="gamedetails",
            name="q2",
            field=models.CharField(
                choices=[("-1", "-1"), ("1", "1"), ("0", "0")],
                default="0",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="gamedetails",
            name="q3",
            field=models.CharField(
                choices=[("-1", "-1"), ("1", "1"), ("0", "0")],
                default="0",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="gamedetails",
            name="q4",
            field=models.CharField(
                choices=[("-1", "-1"), ("1", "1"), ("0", "0")],
                default="0",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="gamedetails",
            name="q5",
            field=models.CharField(
                choices=[("-1", "-1"), ("1", "1"), ("0", "0")],
                default="0",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="gamedetails",
            name="q6",
            field=models.CharField(
                choices=[("-1", "-1"), ("1", "1"), ("0", "0")],
                default="0",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="gamedetails",
            name="q7",
            field=models.CharField(
                choices=[("-1", "-1"), ("1", "1"), ("0", "0")],
                default="0",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="gamedetails",
            name="q8",
            field=models.CharField(
                choices=[("-1", "-1"), ("1", "1"), ("0", "0")],
                default="0",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="gamedetails",
            name="q9",
            field=models.CharField(
                choices=[("-1", "-1"), ("1", "1"), ("0", "0")],
                default="0",
                max_length=10,
            ),
        ),
    ]
