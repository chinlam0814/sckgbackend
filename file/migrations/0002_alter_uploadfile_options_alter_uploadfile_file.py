# Generated by Django 5.0.3 on 2024-04-01 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadfile',
            options={'verbose_name': 'File'},
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to='upload/'),
        ),
    ]
