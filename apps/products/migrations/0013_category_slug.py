# Generated by Django 4.1.3 on 2022-11-25 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0012_sections_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(default=None),
        ),
    ]
