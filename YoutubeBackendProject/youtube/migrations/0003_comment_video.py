# Generated by Django 3.2.6 on 2021-08-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0002_rename_youtube_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.CharField(default='Default Value', max_length=150),
        ),
    ]