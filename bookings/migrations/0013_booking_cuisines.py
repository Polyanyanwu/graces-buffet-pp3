# Generated by Django 3.2 on 2022-05-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0012_alter_booking_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='cuisines',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
