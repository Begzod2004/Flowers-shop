# Generated by Django 4.1.3 on 2022-11-25 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0004_alter_cart_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="id",
            field=models.UUIDField(
                default="334179", editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
