# Generated by Django 4.1.2 on 2022-11-17 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_account_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(db_index=True, max_length=50, null=True, unique=True, verbose_name='Email'),
        ),
    ]