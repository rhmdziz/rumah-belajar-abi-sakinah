# Generated by Django 4.2.7 on 2023-12-02 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Blog',
        ),
    ]
