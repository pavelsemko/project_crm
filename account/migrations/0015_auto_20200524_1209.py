# Generated by Django 3.0.6 on 2020-05-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20200523_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='manager',
            new_name='closer',
        ),
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
