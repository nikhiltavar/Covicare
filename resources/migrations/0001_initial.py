# Generated by Django 4.0 on 2022-04-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone', models.DecimalField(decimal_places=0, max_digits=12)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('totalPatients', models.DecimalField(decimal_places=0, max_digits=5)),
                ('totalBeds', models.DecimalField(decimal_places=0, max_digits=5)),
                ('availableBeds', models.DecimalField(decimal_places=0, max_digits=5)),
                ('totalVentillators', models.DecimalField(decimal_places=0, max_digits=5)),
                ('availableVentillators', models.DecimalField(decimal_places=0, max_digits=5)),
                ('totalInfusionPump', models.DecimalField(decimal_places=0, max_digits=5)),
                ('availableInfusionPump', models.DecimalField(decimal_places=0, max_digits=5)),
                ('totalO2Delivery', models.DecimalField(decimal_places=0, max_digits=5)),
                ('availableO2Delivery', models.DecimalField(decimal_places=0, max_digits=5)),
                ('O2cylinder', models.DecimalField(decimal_places=0, max_digits=5)),
            ],
        ),
    ]
