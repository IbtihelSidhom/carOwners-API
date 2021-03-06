# Generated by Django 2.2.6 on 2019-10-21 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=200)),
                ('car_model', models.CharField(max_length=200)),
                ('car_model_year', models.IntegerField()),
                ('car_vin', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'owners',
            },
        ),
    ]
