# Generated by Django 5.0.3 on 2024-05-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0004_texts_json_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='texts',
            name='created_by',
            field=models.TextField(default=''),
        ),
    ]
