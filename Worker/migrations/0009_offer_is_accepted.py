# Generated by Django 3.2.4 on 2021-11-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Worker', '0008_auto_20211127_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
