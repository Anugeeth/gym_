# Generated by Django 3.0.4 on 2020-03-13 13:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_auto_20200307_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='renew_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 13, 13, 40, 31, 483646, tzinfo=utc), verbose_name='Date renewed'),
            preserve_default=False,
        ),
    ]