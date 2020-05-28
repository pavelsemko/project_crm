# Generated by Django 3.0.6 on 2020-05-25 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_planning'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='comment',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='planning',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planning_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planning',
            name='type',
            field=models.TextField(choices=[('First call', 'First call'), ('Callback', 'Callback'), ('Platform show', 'Platform show'), ('Account fixing', 'Account fixing'), ('Trial deal', 'Trial deal'), ('Deposit', 'Deposit')], default='new', max_length=50),
        ),
        migrations.AlterField(
            model_name='leads',
            name='about_client',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='leads',
            name='source',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]