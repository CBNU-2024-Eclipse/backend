# Generated by Django 5.0.6 on 2024-06-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_alter_plantanalysis_id_alter_plantenvironment_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plantenvironment",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
