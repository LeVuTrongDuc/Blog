# Generated by Django 4.2.5 on 2023-12-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_body_post_content_remove_post_audio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='audio',
            field=models.FileField(null=True, upload_to='media/music'),
        ),
    ]
