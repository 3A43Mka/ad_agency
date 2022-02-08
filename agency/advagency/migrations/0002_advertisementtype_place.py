# Generated by Django 4.0.2 on 2022-02-05 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advagency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementType',
            fields=[
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('type_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='advagency.advertisementtype')),
            ],
        ),
    ]