# Generated by Django 4.0.1 on 2022-01-29 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0003_rename_datapredictions_dataprediction'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunningJobs',
            fields=[
                ('datafile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='predict.datafile')),
            ],
        ),
    ]
