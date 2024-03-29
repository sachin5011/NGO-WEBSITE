# Generated by Django 4.2.8 on 2023-12-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('image1', models.FileField(max_length=300, upload_to='mission/')),
                ('image2', models.FileField(max_length=300, upload_to='mission/')),
            ],
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('desc', models.TextField()),
                ('image1', models.FileField(max_length=300, upload_to='vision/')),
                ('image2', models.FileField(max_length=300, upload_to='vision/')),
            ],
        ),
        migrations.RenameField(
            model_name='about',
            old_name='charity_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='charity_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='mission_desc',
        ),
        migrations.RemoveField(
            model_name='about',
            name='mission_title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='vision_desc',
        ),
        migrations.RemoveField(
            model_name='about',
            name='vision_title',
        ),
    ]
