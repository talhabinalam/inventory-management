# Generated by Django 5.1.2 on 2024-11-11 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_remove_order_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]