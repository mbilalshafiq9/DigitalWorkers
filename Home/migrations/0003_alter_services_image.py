# Generated by Django 3.2.4 on 2021-11-14 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]