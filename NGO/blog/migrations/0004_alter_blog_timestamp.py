# Generated by Django 4.2.8 on 2023-12-24 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 9, 24, 17, 528688, tzinfo=datetime.timezone.utc)),
        ),
    ]
