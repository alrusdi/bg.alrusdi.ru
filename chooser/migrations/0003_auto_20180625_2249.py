# Generated by Django 2.0.6 on 2018-06-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chooser', '0002_play_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='played_at',
            field=models.DateField(),
        ),
    ]
