# Generated by Django 3.0.3 on 2020-11-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecartApp', '0004_auto_20201122_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='item_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]