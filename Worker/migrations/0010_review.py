# Generated by Django 3.2.4 on 2021-11-29 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0004_alter_message_is_read'),
        ('Worker', '0009_offer_is_accepted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='Buyer.buyer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='Worker.order')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='worker', to='Worker.worker')),
            ],
        ),
    ]
