# Generated by Django 3.2.4 on 2021-11-15 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Worker', '0002_auto_20211115_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker',
            old_name='skils',
            new_name='skills',
        ),
    ]