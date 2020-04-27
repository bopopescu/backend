# Generated by Django 3.0.5 on 2020-04-27 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ShippingMethod', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('street', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('state', models.CharField(max_length=30, null=True)),
                ('zipcode', models.IntegerField(default=0, null=True)),
                ('total_rating', models.IntegerField(default=0, null=True)),
                ('rating_count', models.IntegerField(default=0, null=True)),
                ('rating', models.DecimalField(decimal_places=1, default=1.0, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='StationRobot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShippingMethod.Robot')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Station.Station')),
            ],
        ),
        migrations.CreateModel(
            name='StationDrone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShippingMethod.Drone')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Station.Station')),
            ],
        ),
    ]
