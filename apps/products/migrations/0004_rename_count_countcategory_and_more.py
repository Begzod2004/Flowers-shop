# Generated by Django 4.1.3 on 2022-12-05 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_product_count_alter_product_length_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Count",
            new_name="CountCategory",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="count",
            new_name="countCategory",
        ),
    ]
