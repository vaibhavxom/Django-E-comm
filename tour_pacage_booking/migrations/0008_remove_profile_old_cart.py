# Generated by Django 5.1 on 2024-09-15 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour_pacage_booking', '0007_profile_old_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='old_cart',
        ),
    ]
