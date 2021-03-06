# Generated by Django 3.0.4 on 2020-03-20 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('adm_no', models.AutoField(primary_key=True, serialize=False, verbose_name='Admission no')),
                ('age', models.IntegerField(verbose_name='Age of the person')),
                ('weight', models.FloatField(verbose_name='weight of the person')),
                ('height', models.FloatField(verbose_name='height of the person')),
                ('duration', models.IntegerField(verbose_name='subscription duration')),
                ('phone', models.IntegerField(max_length=10, verbose_name='phone no')),
                ('date_joined', models.DateField(verbose_name='Date joined')),
                ('exp_date', models.DateField(verbose_name='Date renewed')),
                ('address', models.CharField(max_length=500)),
                ('payment_status', models.BooleanField(default=True, verbose_name='subscribed or not')),
                ('photo', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
