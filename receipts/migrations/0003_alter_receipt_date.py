# Generated by Django 5.0.1 on 2024-02-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("receipts", "0002_rename_accountmodel_account_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipt",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
