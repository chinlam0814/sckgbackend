# Generated by Django 5.0.3 on 2024-08-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0008_fileinfo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file_text',
            field=models.TextField(default='', null=True),
        ),
    ]
