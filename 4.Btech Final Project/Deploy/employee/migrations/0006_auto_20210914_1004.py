# Generated by Django 2.2.5 on 2021-09-14 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20210204_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='UPLOAD_ROAD_IMAGE',
            new_name='UPLOAD_EMOTION_IMAGE',
        ),
    ]
