# Generated by Django 5.0.3 on 2024-05-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_alter_uploadfile_options_alter_uploadfile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
