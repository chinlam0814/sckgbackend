# Generated by Django 5.0.3 on 2024-05-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_account_join_date_admin_join_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(default='man', max_length=7),
        ),
        migrations.AddField(
            model_name='admin',
            name='gender',
            field=models.CharField(default='man', max_length=7),
        ),
    ]
