# Generated by Django 4.2.8 on 2023-12-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='carousel_img',
            field=models.FileField(max_length=300, null=True, upload_to='carousel/'),
        ),
    ]