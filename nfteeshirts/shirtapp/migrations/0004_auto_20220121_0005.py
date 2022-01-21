# Generated by Django 3.2.11 on 2022-01-21 00:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirtapp', '0003_auto_20220119_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='hex',
            field=models.CharField(default='#FFFFFF', max_length=10),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 0, 5, 9, 372658)),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='last_order',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 0, 5, 9, 372682)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 21, 0, 5, 9, 373441)),
        ),
    ]
