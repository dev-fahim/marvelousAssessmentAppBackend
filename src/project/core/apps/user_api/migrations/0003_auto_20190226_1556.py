# Generated by Django 2.1.7 on 2019-02-26 09:56

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0002_auto_20190225_2311'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='mainuser',
            managers=[
                ('client', django.db.models.manager.Manager()),
            ],
        ),
    ]
