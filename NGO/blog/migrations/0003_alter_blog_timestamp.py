# Generated by Django 4.2.8 on 2023-12-24 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 8, 43, 53, 423793, tzinfo=datetime.timezone.utc)),
        ),
    ]