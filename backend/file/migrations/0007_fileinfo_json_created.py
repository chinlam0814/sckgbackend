# Generated by Django 5.0.3 on 2024-05-16 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0006_uploadfile_file_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileinfo',
            name='json_created',
            field=models.JSONField(default=dict),
        ),
    ]
