# Generated by Django 2.0.3 on 2018-05-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pk_stops', '0016_booking_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='lat',
            field=models.FloatField(default=13.0587),
        ),
        migrations.AddField(
            model_name='organisation',
            name='lon',
            field=models.FloatField(default=80.2641),
        ),
    ]