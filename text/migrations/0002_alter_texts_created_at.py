# Generated by Django 5.0.3 on 2024-04-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texts',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
