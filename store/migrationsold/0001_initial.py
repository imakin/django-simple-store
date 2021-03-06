# Generated by Django 2.1.5 on 2019-12-22 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('phone_number', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('status', models.TextField()),
                ('complete', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('sku', models.CharField(max_length=64, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('stock', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('additional_image_links', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Storesetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_currency', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('price_multiplier', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='store.Product'),
        ),
        migrations.AddField(
            model_name='customer',
            name='cart',
            field=models.ManyToManyField(to='store.Product'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Customer'),
        ),
    ]
