# Generated by Django 3.0.3 on 2020-11-22 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecartApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generateitem',
            name='item_description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
