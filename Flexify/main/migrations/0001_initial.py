# Generated by Django 4.1.13 on 2024-07-23 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Diet",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "username",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FoodItem",
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
                ("text", models.CharField(max_length=200)),
                (
                    "diet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.diet"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="diet",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.user"
            ),
        ),
    ]
