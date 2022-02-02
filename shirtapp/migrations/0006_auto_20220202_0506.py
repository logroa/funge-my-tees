# Generated by Django 3.2.11 on 2022-02-02 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirtapp', '0005_auto_20220121_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='last_order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_num',
        ),
        migrations.AddField(
            model_name='buyer',
            name='name',
            field=models.CharField(default='none', max_length=255),
        ),
        migrations.AddField(
            model_name='buyer',
            name='phone_number',
            field=models.CharField(default='xxx', max_length=15),
        ),
        migrations.AddField(
            model_name='order',
            name='fulfilled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='order_price',
            field=models.FloatField(default=20),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 5, 6, 31, 475410)),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='email',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 5, 6, 31, 480303)),
        ),
    ]
