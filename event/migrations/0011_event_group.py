# Generated by Django 3.0.3 on 2020-09-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20200913_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='group',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
