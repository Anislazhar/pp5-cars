# Generated by Django 3.2.25 on 2024-07-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_banner',
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='../dinner.219fa9d437e9', upload_to='images/'),
        ),
    ]
