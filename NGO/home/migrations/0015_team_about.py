# Generated by Django 4.2.8 on 2023-12-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_delete_causes'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
