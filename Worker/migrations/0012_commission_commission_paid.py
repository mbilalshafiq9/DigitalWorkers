# Generated by Django 3.2.4 on 2021-12-10 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Worker', '0011_auto_20211129_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission_Paid',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('pay_amount', models.IntegerField(null=True)),
                ('paid_at', models.DateTimeField(auto_now_add=True)),
                ('paid_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paid_by', to='Worker.worker')),
            ],
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='worker_com', to='Worker.worker')),
            ],
        ),
    ]
