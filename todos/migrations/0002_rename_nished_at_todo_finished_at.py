# Generated by Django 5.1.3 on 2024-11-19 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='nished_at',
            new_name='finished_at',
        ),
    ]
