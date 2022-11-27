# Generated by Django 4.1.3 on 2022-11-24 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0011_alter_image_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="sections",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.sectionscategory",
            ),
            preserve_default=False,
        ),
    ]