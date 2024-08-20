# Generated by Django 5.0.3 on 2024-07-17 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0006_alter_texts_json_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='texts',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='texts',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
