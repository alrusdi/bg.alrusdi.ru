# Generated by Django 2.0.6 on 2018-06-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chooser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='play',
            name='mode',
            field=models.CharField(choices=[('PLAYED', 'Сыграно'), ('REJECTED', 'Отказ')], default='PLAYED', max_length=50),
        ),
    ]