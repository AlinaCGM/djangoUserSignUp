# Generated by Django 4.2.7 on 2023-11-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0005_remove_user_avatar_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.URLField(blank=True, null=True),
        ),
    ]