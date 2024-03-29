# Generated by Django 4.2.8 on 2023-12-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_imagecategory_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=300)),
                ('building_no', models.CharField(blank=True, max_length=300)),
                ('district', models.CharField(blank=True, max_length=300)),
                ('state', models.CharField(blank=True, max_length=300)),
                ('pincode', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
                ('email', models.CharField(blank=True, max_length=300)),
                ('phone', models.CharField(blank=True, max_length=300)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
