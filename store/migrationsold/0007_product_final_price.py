# Generated by Django 2.1.5 on 2019-12-23 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20191222_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='final_price',
            field=models.IntegerField(default=0),
        ),
    ]
