# Generated by Django 4.2.8 on 2023-12-27 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 27, 12, 22, 33, 668474, tzinfo=datetime.timezone.utc)),
        ),
    ]