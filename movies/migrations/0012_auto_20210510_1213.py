# Generated by Django 3.1.5 on 2021-05-10 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20210510_1211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='url',
            new_name='slug',
        ),
    ]