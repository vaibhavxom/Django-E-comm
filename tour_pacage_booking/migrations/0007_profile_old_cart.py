# Generated by Django 5.1 on 2024-09-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_pacage_booking', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
