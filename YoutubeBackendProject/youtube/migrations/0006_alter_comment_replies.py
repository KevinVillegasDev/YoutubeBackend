# Generated by Django 3.2.6 on 2021-08-18 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0005_alter_comment_replies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='replies',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]