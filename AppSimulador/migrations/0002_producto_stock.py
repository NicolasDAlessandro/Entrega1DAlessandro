# Generated by Django 4.0.4 on 2022-04-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSimulador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
