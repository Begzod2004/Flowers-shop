# Generated by Django 4.1.3 on 2022-12-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="count",
            name="title",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="length",
            name="title",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="width",
            name="title",
            field=models.CharField(max_length=50),
        ),
    ]
