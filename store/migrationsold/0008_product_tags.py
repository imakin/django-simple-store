# Generated by Django 2.1.5 on 2019-12-23 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_final_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]
