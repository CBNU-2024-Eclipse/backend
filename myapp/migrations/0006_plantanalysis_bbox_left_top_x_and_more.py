# Generated by Django 5.0.6 on 2024-06-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0005_alter_plantanalysis_current_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="plantanalysis",
            name="bbox_left_top_x",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="plantanalysis",
            name="bbox_left_top_y",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="plantanalysis",
            name="bbox_right_bottom_x",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="plantanalysis",
            name="bbox_right_bottom_y",
            field=models.FloatField(null=True),
        ),
    ]
