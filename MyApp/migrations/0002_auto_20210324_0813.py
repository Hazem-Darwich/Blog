# Generated by Django 3.1.7 on 2021-03-24 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topics',
            old_name='board',
            new_name='name',
        ),
    ]
