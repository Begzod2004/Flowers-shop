# Generated by Django 4.1.3 on 2022-11-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0009_rename_product_id_image_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gallery",
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
                ("image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Sections",
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
                ("title", models.CharField(max_length=30)),
                ("image", models.ImageField(upload_to="CarsImages")),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="SectionsCategory",
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
                ("title", models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name="flower",
            name="product_id",
        ),
        migrations.RemoveField(
            model_name="productreview",
            name="review_title",
        ),
        migrations.AddField(
            model_name="product",
            name="color",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(upload_to="CarsImages"),
        ),
        migrations.DeleteModel(
            name="Color",
        ),
        migrations.DeleteModel(
            name="Flower",
        ),
    ]