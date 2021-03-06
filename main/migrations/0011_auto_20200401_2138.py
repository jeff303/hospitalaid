# Generated by Django 3.0.4 on 2020-04-01 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_auto_20200401_2123"),
    ]

    operations = [
        migrations.AddField(
            model_name="aidrequest",
            name="equipment_brand",
            field=models.CharField(
                blank=True, help_text="only for equipment repair", max_length=16
            ),
        ),
        migrations.AddField(
            model_name="aidrequest",
            name="equipment_model",
            field=models.CharField(
                blank=True, help_text="only for equipment repair", max_length=16
            ),
        ),
        migrations.AddField(
            model_name="aidrequest",
            name="equipment_serialno",
            field=models.CharField(
                blank=True, help_text="only for equipment repair", max_length=16
            ),
        ),
    ]
