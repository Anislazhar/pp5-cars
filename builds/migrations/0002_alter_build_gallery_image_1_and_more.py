# Generated by Django 5.0.7 on 2024-07-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='gallery_image_1',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='build',
            name='gallery_image_2',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='build',
            name='gallery_image_3',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='build',
            name='gallery_image_4',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='build',
            name='main_image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
