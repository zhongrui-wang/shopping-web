# Generated by Django 3.0rc1 on 2019-12-01 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.FloatField(default=500),
            preserve_default=False,
        ),
    ]