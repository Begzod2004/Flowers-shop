# Generated by Django 4.1.3 on 2022-11-17 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0003_order_images_order_images2_order_images3_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="images",
            field=models.ImageField(null=True, upload_to="apps/order/"),
        ),
    ]
