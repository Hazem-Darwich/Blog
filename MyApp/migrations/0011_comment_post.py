# Generated by Django 3.1.7 on 2021-04-05 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='MyApp.post'),
        ),
    ]
