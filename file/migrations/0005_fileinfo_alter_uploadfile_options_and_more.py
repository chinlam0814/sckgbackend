# Generated by Django 5.0.3 on 2024-05-04 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_uploadfile_created_at_uploadfile_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('created_by', models.TextField(default='')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'File',
            },
        ),
        migrations.AlterModelOptions(
            name='uploadfile',
            options={},
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='uploadfile',
            name='name',
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(null=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='file.fileinfo'),
        ),
    ]
