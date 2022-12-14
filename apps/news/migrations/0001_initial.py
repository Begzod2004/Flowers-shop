# Generated by Django 4.1.3 on 2022-11-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="New",
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
                ("title", models.CharField(max_length=20)),
                ("image", models.ImageField(upload_to="newsImg/")),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]
