# Generated by Django 4.2.8 on 2024-01-08 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blog_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 8, 14, 59, 22, 85771, tzinfo=datetime.timezone.utc)),
        ),
    ]
