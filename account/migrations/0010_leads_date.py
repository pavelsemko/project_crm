# Generated by Django 3.0.6 on 2020-05-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200523_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='date',
            field=models.DateField(null=True),
        ),
    ]