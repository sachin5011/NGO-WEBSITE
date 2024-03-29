# Generated by Django 4.2.8 on 2023-12-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='pay_amount',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='payments',
            name='pay_mode',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='payments',
            name='pay_name',
            field=models.CharField(blank=True, default='Anonymous', max_length=300),
        ),
        migrations.AlterField(
            model_name='payments',
            name='pay_trans_id',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
