# Generated by Django 4.1.3 on 2022-11-25 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0013_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(),
        ),
    ]
