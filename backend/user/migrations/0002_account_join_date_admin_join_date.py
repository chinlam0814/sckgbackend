# Generated by Django 5.0.3 on 2024-04-11 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='join_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='join_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
