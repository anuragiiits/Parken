# Generated by Django 2.0.3 on 2018-03-28 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rate', models.FloatField(default=10)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_booked', models.BooleanField(default=False)),
                ('booked_from', models.DateTimeField(auto_now=True)),
                ('booked_till', models.DateTimeField()),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pk_stops.Organisation')),
            ],
        ),
    ]
