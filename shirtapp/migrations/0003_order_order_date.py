# Generated by Django 4.0.3 on 2022-04-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirtapp', '0002_remove_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateField(null=True),
        ),
    ]
