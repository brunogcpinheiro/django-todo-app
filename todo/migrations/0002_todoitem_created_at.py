# Generated by Django 3.0.4 on 2020-03-18 01:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='created_at',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
