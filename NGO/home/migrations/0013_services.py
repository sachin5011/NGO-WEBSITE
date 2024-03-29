# Generated by Django 4.2.8 on 2023-12-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_address_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('sub_title', models.CharField(blank=True, max_length=500)),
                ('image', models.FileField(blank=True, max_length=500, upload_to='services/')),
            ],
        ),
    ]
