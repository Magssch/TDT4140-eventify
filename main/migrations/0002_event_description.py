# Generated by Django 2.1.5 on 2019-02-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='Enter content'),
            preserve_default=False,
        ),
    ]
