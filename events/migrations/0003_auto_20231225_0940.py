# Generated by Django 3.2.7 on 2023-12-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
