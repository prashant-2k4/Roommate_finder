# Generated by Django 5.1.7 on 2025-03-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_room_location_alter_room_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='room_images/'),
        ),
    ]
