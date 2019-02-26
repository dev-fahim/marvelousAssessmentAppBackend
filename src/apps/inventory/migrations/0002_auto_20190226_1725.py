# Generated by Django 2.1.7 on 2019-02-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0004_auto_20190226_1559'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorymanagerconnectionbridge',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='inventorymanagerconnectionbridge',
            name='main_user',
        ),
        migrations.RemoveField(
            model_name='inventorymanagerconnectionbridge',
            name='manager',
        ),
        migrations.AddField(
            model_name='inventory',
            name='managers',
            field=models.ManyToManyField(related_name='inventories', to='user_api.ManagerUser'),
        ),
        migrations.DeleteModel(
            name='InventoryManagerConnectionBridge',
        ),
    ]
