# Generated by Django 4.1 on 2022-09-01 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user", models.CharField(max_length=200, verbose_name="User")),
                ("path", models.CharField(max_length=200, verbose_name="Request Path")),
                ("count", models.PositiveIntegerField(default=1, verbose_name="Number of requests")),
            ],
        ),
    ]
