# Generated by Django 3.1.7 on 2021-03-27 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_auto_20210327_0911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='borad',
            new_name='board',
        ),
    ]
