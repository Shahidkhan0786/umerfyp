# Generated by Django 3.2.3 on 2021-05-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_auto_20210528_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='package',
            field=models.CharField(choices=[('basic', 'Basic'), ('standard', 'Standard'), ('prenium', 'Orenium')], default='', max_length=200),
            preserve_default=False,
        ),
    ]
