# Generated by Django 2.1.5 on 2019-02-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='event_image'),
        ),
    ]
