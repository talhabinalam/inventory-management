# Generated by Django 5.1.2 on 2024-11-11 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
    ]