# Generated by Django 3.0.6 on 2020-05-25 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_leads_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update', models.DateTimeField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]