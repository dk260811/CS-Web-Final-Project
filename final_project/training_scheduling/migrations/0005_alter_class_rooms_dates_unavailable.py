# Generated by Django 4.1.3 on 2022-12-26 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_scheduling', '0004_alter_students_training_day_arrival_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_rooms',
            name='dates_unavailable',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
