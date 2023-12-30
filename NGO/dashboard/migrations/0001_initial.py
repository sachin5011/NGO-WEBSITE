# Generated by Django 4.2.8 on 2023-12-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_name', models.CharField(default='Anonymous', max_length=300)),
                ('pay_mode', models.CharField(default=True, max_length=100)),
                ('pay_amount', models.CharField(default=True, max_length=100)),
                ('pay_trans_id', models.CharField(default=True, max_length=200)),
            ],
        ),
    ]