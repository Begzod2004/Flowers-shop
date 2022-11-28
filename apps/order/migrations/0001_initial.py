# Generated by Django 4.1.3 on 2022-11-28 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (0, "New"),
                            (1, "Prosess"),
                            (2, "Canceled"),
                            (3, "Finished"),
                        ],
                        default=0,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("product", models.ManyToManyField(to="products.product")),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
