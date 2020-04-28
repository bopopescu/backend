
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '__first__'),
        ('Station', '__first__'),
        ('Address', '0001_initial'),
        ('Tracking', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=30, null=True)),
                ('item_info', models.CharField(max_length=30, null=True)),
                ('capacity', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('create_time', models.DateTimeField(null=True)),
                ('depart_time', models.DateTimeField(null=True)),
                ('pickup_time', models.DateTimeField(null=True)),
                ('complete_time', models.DateTimeField(null=True)),
                ('shipping_method', models.CharField(max_length=30, null=True)),
                ('shipping_number', models.IntegerField(default=1)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('feedback', models.IntegerField(null=True)),
                ('from_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromaddress', to='Address.Address')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Station.Station')),
                ('to_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toaddress', to='Address.Address')),
                ('tracking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tracking.Tracking')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
        ),
    ]
