# Generated by Django 3.2.11 on 2022-01-19 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirtapp', '0002_auto_20220118_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 19, 9, 6, 45, 567040)),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='last_order',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 19, 9, 6, 45, 567075)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 19, 9, 6, 45, 568209)),
        ),
    ]
