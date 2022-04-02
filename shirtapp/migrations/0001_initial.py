# Generated by Django 4.0.3 on 2022-04-02 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(default='xxx', max_length=15)),
                ('name', models.CharField(default='none', max_length=255)),
                ('created_on', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pic1_img_url', models.CharField(max_length=100)),
                ('pic1_title', models.CharField(default='Front', max_length=100)),
                ('pic2_img_url', models.CharField(max_length=100)),
                ('pic2_title', models.CharField(default='Back', max_length=100)),
                ('price', models.IntegerField(default=20)),
                ('available', models.BooleanField(default=True)),
                ('hex', models.CharField(default='#FFFFFF', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shirt_size', models.CharField(max_length=10)),
                ('order_date', models.DateField(null=True)),
                ('order_price', models.FloatField(default=20)),
                ('order_uuid', models.CharField(max_length=100)),
                ('confirmed', models.FloatField(default=False)),
                ('fulfilled', models.BooleanField(default=False)),
                ('advocate', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shirtapp.advocate')),
                ('shirt', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shirtapp.shirt')),
            ],
        ),
    ]
