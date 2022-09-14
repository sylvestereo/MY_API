# Generated by Django 4.1.1 on 2022-09-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=255)),
                ("price", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("overview", models.TextField()),
                ("img", models.URLField()),
            ],
        ),
    ]
